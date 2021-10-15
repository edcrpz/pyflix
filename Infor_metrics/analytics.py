import pandas as pd 
from boto3 import Session
from botocore.exceptions import ClientError
from io import StringIO
import boto3


def create_session(account: str = "", region: str = "") -> "boto3.Session":
    """Return a boto3 session object"""

    if not account:
        account = None

    if not region:
        region = None

    return Session(profile_name=account, region_name=region)

def s3_get_object(bucket: str, key: str, session: "boto3.Session") -> dict:
    """Get an object in s3"""

    response = {}
    try:
        response = session.client("s3").get_object(Bucket=bucket, Key=key)
        
    except ClientError as error:
        raise RuntimeError(error) from error
    return response


def list_s3_objects(bucket, prefix):
    
    object_list = []
    
    for obj in bucket.objects.filter(prefix):
        object_list.append(obj)
        
    return object_list

def payload2df(obj):
    body = obj['Body']
    csv_string = body.read().decode('utf-8')

    df = pd.read_csv(StringIO(csv_string))
    
    return df

def metrics_pp(df):
    df.columns=df.columns.str.replace("-","")
    df.columns=df.columns.str.replace(" ","")
    
    df['timestamp'] = pd.to_datetime(df['Time'])
    df = df.set_index('timestamp')
    
    return df

def summary_stats(df):
    stats = df.describe().transpose()
    
    return stats

# Under
# over
# average
# No data warning

def simple_threshhold(data, name = 'testmetric', upper_bound=None, lower_bound=None):
    
    response = {}
    response['process'] = "SimpleThreshhold"
    
    if lower_bound and min(data) < lower_bound:
        
        response['alarm'] = True
        response['comment'] = f"The value for {name} is below {lower_bound}." 
    
    if upper_bound and max(data) < upper_bound:
        
        response['alarm'] = True
        response['comment'] = f"The value for {name} is above {upper_bound}." 
    
    else:
        response['alarm'] = False
        
    return response
    
# TODO: write loop that iterates over objects in s3 bucket    
session = create_session(account= 'int', region= 'us-east-1')
    
obj = s3_get_object(bucket= "infor-int-appdata-us-east-1",
              key ="tam/dashdata/csv/1631345019/ELB Latency_ResponseTime - All-data-as-seriestocolumns-2021-09-10 17_22_06.csv",
             session = session)

df = payload2df(obj)

simple_threshhold(df['241AverageTargetResponseTime'], upper_bound=23, lower_bound=.3, name='Target Response Time')


