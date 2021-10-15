#!/usr/bin/env python3

import argparse
import textwrap
import subprocess
import os
import shutil
from datetime import datetime
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from selenium import webdriver
import os
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import sys
import yaml
from datetime import datetime
import logging
from selenium.webdriver.common.action_chains import ActionChains
import boto3
import botocore
from botocore.exceptions import ClientError
import glob


cwd = os.getcwd()
#  print(cwd)
sys.path.append(f"{cwd}")
downloads = str(os.path.join(Path.home(), "Downloads"))
metrics_path = downloads + '/metrics'

now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H-%M-%S")

login_url = "https://grafana.monocle.cts.infor.com/d/6ikQewuMz/csf-dashboards-mt-capacity-management?orgId=1"

options = webdriver.ChromeOptions()
prefs = {'download.default_directory': metrics_path}     # Default download location of Chrome set to metrics_path
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome('chromedriver', chrome_options=options)
options.headless = True


def monocle_login():
    driver.get(login_url)
    print("\nLogging in...\n")
    sleep(60)  # to have more time when logging in manually using Infor SSO / 2Factor ID


def dashboard2csv(url_dictionary):
    for url in url_dictionary:                                      # For each URL in dictionary, call download_raw()
        download_raw(url_dictionary[url][0])
        print(f"CSV file saved at {metrics_path}")
    driver.quit()


def dashboard2pdf(url_dictionary):
    for url in url_dictionary:                                     # For each URL in dictionary, call take_screenshot()
        take_screenshot(url_dictionary[url][0], url_dictionary[url][1])
    driver.quit()


def dashboard2all(url_dictionary):
    for url in url_dictionary:                                          # For each URL in dictionary, call get_all()
        get_all(url_dictionary[url][0], url_dictionary[url][1])
    driver.quit()


def take_screenshot(url, filepath):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')    # Opens a New Tab
    driver.get(url)                                                          # Opens and loads URL
    driver.fullscreen_window()                                               # Full-screen window
    sleep(10)                                                                    # Gives time to load
    driver.save_screenshot(filepath)                                         # Take screenshot
    print("Screenshot saved at " + filepath)


def download_raw(url, max_retries=10):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    driver.get(url)
    driver.fullscreen_window()
    sleep(15)

    # driver.find_element_by_class_name("css-132xth5").click()
    # sleep(3)
    # driver.find_element_by_class_name("css-1pcbsvw-button").click()
    # sleep(3)
    # action = ActionChains(driver)
    # action.send_keys('c').send_keys('o').send_keys('o').send_keys('r').send_keys(Keys.ENTER).perform()
    # sleep(2)
    # driver.find_element_by_class_name("css-132xth5").click()

    download_success = False
    while download_success is False:
        try:
            print("Locating panel title...")
            link = driver.find_element_by_class_name("panel-title-text")  # Panel Title
            link.click()
            sleep(2)
            print("Locating Inspect button...")
            driver.find_element_by_tag_name('body').send_keys('i')  # Inspect button
            download_success = True

        except NoSuchElementException:
            print("Oops! Error: NoSuchElementException. The web page may not be ready. Try again.")
            sleep(10)
            
    retry_counter = 0
    while retry_counter <= max_retries:
        retry_counter += 1
        try:
            sleep(3)
            print("Locating Download CSV button...")
            download = driver.find_element_by_class_name('css-1beih13')  # Download CSV button
            print("Clicking Download CSV button...")
            download.click()                                                 # Click button
            sleep(2)
            break

        except NoSuchElementException:
            print("Oops! Error: NoSuchElementException. The web page may not be ready. Try again.")
            sleep(10)


def get_all(url, filepath, max_retries=5):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    driver.get(url)
    driver.fullscreen_window()
    sleep(10)
    driver.save_screenshot(filepath)
    print("Screenshot saved at " + filepath)

    download_success = False
    while download_success is False:
        try:
            print("Locating panel title...")
            link = driver.find_element_by_class_name("panel-title-text")  # Panel Title
            link.click()
            sleep(2)
            print("Locating Inspect button...")
            driver.find_element_by_tag_name('body').send_keys('i')  # Inspect button
            download_success = True

        except NoSuchElementException:
            print("Oops! Error: NoSuchElementException. The web page may not be ready. Try again.")
            sleep(10)

    retry_counter = 0
    while retry_counter <= max_retries:
        retry_counter += 1
        try:
            sleep(3)
            print("Locating Download CSV button...")
            download = driver.find_element_by_class_name('css-1beih13')  # Download CSV button
            print("Clicking Download CSV button...")
            download.click()  # Click button
            sleep(2)
            break

        except NoSuchElementException:
            print("Oops! Error: NoSuchElementException. The web page may not be ready. Try again.")
            sleep(10)


def load_yaml(path):
    with open(path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
                print(exc)


def modify_urls(time_from, time_to='now'):
    str_time_from = str(time_from)
    str_time_to = str(time_to)
    urls = load_yaml('urls.yml')

    for metrics in urls:
        string = urls[metrics][0]
        string = string.replace("{time_from}", str_time_from)  # replace time_from in YAML file with user provided time
        string = string.replace("{time_to}", str_time_to)
        urls[metrics][0] = string  # assign replaced string back to dictionary

        filepath = urls[metrics][1]
        filepath = filepath.replace(filepath, f"{metrics_path}/{filepath}-{dt_string}.png")
        urls[metrics][1] = filepath   # assign replaced string back to dictionary

    return urls   # return dictionary


def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    # Upload the file
    s3_client = boto3.client('s3', region_name='us-east-1')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def s3_upload(output):

    utc_now = (datetime.utcnow())  # well want this outside of func but well keep this here for now

    params = load_yaml('collector_params.yml')

    os.environ['AWS_PROFILE'] = params["account"]
    os.environ['AWS_DEFAULT_REGION'] = params["region"]

    params = load_yaml('collector_params.yml')
    bucket_name = params["s3_bucket"]
    data_folder = params["s3_data_folder"]
    pdf_folder = params["s3_pdf_folder"]
    all_folder = params["s3_all_folder"]

    csv_files = glob.glob(f'{metrics_path}/*.csv')
    pdf_files = glob.glob(f'{metrics_path}/*.png')
    all_files = glob.glob(f'{metrics_path}/*')

    if output == 'csv':
        for filename in csv_files:
            upload_file(
                file_name=filename,
                bucket=bucket_name,
                object_name=f"{data_folder}{utc_now}/{os.path.basename(filename)}")
    elif output == 'pdf':
        for filename in pdf_files:
            upload_file(
                file_name=filename,
                bucket=bucket_name,
                object_name=f"{pdf_folder}{utc_now}/{os.path.basename(filename)}")
    elif output == 'all':
        for filename in all_files:
            upload_file(
                file_name=filename,
                bucket=bucket_name,
                object_name=f"{all_folder}{utc_now}/{os.path.basename(filename)}")

    for files in os.listdir(metrics_path):
        path = os.path.join(metrics_path, files)
        try:
            shutil.rmtree(path)
            print(f"File {path} is successfully deleted!")
        except OSError:
            os.remove(path)


def convert_to_ms(time):
    dt_obj = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    epoch_ms = dt_obj.timestamp() * 1000
    return epoch_ms


def parse_and_extract():
    if not os.path.exists(metrics_path):   # creates ~/Downloads/metrics folder if not existing
        os.makedirs(metrics_path)

    # Interprets arguments from user

    modes = ['pdf', 'csv', 'all']

    parser = argparse.ArgumentParser(description='Generate metrics report - screenshots, raw data in CSV, or both',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
                                     Example usage:
                                     --------------------------------
                                     Gather data in CSV format from Aug. 29, 2021 9:00 PM - 11:00 PM Local time:
                                     
                                     #######
                                     ./metrics.py -o csv -sd 2021-08-29 -st 21:00:00 -ed 2021-08-29 -et 23:00:00
                                     #######
                                     
                                     The timezone of the data itself will depend on User's Monocle settings (usually CST/CDT).
                                     File and folder names with timestamps are written from Local PC / Workspace timezone.
                                     
                                     
                                     '''))

    parser.add_argument('-o', '--output', type=str, required=True, choices=modes,
                        help='set mode of operation to obtain desired output pdf/csv/all)')
    parser.add_argument('-sd', '--start_date', type=str, required=True, help='Start Time in YY:MM:DD format')
    parser.add_argument('-ed', '--end_date', type=str, help='End Time in YY:MM:DD format')
    parser.add_argument('-st', '--start_time', type=str, required=True, help='Start Time in hh:mm:ss format')
    parser.add_argument('-et', '--end_time', type=str, required=True, help='End Time in hh:mm:ss format')
    args = parser.parse_args()

    epoch_from = int(convert_to_ms(args.start_date + " " + args.start_time))
    epoch_to = int(convert_to_ms(args.end_date + " " + args.end_time))

    urls_dict = modify_urls(time_from=epoch_from, time_to=str(epoch_to))
    # urls_dict calls function modify urls to modify URL's start time and end time from arguments stored in args_dict
    # modify_urls() returns a dictionary that contains URLs and file path

    if args.output == 'pdf':
        monocle_login()               # Calls monocle_login() function that performs login to MT Dashboard
        dashboard2pdf(urls_dict)
        # Supplies dictionary (urls_dict) and calls function that opens a new tab and
        # perform PDF specific operations

    elif args.output == 'csv':
        monocle_login()
        dashboard2csv(urls_dict)      # CSV specific operations
    elif args.output == 'all':
        print("This mode is to gather BOTH raw data and screenshots")
        monocle_login()
        dashboard2all(urls_dict)      # BOTH CSV and PDF operations

    else:
        print('''
        Please specify correct mode:\n
        screenshot - gather screenshots to save in PDF
        raw - gather raw data in CSV
        ''')

    s3_upload(args.output)
    # Calls s3_upload function which uploads the generated desired output files to corresponding S3 destination path and
    # delete files generated locally (~/Downloads/metrics/*)


if __name__ == "__main__":
    parse_and_extract()
