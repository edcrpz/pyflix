#!/usr/bin/env python3

import argparse
import os
import textwrap

def parse():

    parser = argparse.ArgumentParser(description='Lists TAM instances by farm or region',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
                                     \n
                                     Example usage:
                                     --------------------------------

                                     check_instances.py -r us-east-1
                                     check_instances.py -r us-east-1 -f 204
                                     check_instances.py --region us-east-1 --farm 207 --type jb

                                     
                                     Values
                                     --------------------------------

                                     Farms

                                     US-EAST-1          = 201 - 207
                                     AP-SOUTHEAST-2     = 231
                                     CA-CENTRAL-1       = 241
                                     EU-CENTRAL-1       = 210
                                     EU-WEST-2          = 220

                                     Regions-API:

                                     US East 1                    = us-east-1
                                     South East Asia Pacific 2    = ap-southeast-2
                                     Central CA 1                 = ca-central-1
                                     Central Europe               = eu-central-1
                                     West Europe 2                = eu-west-2
                                     
                                     EC2 Instance Types:
                                     
                                     Jboss                        = jb
                                     CS                           = cs
                                     WS                           = ws
                                     PA                           = pa
                                     Batch Executor               = be

                                     '''))

    parser.add_argument('-r', '--region', type=str, required=True, help='desired Region')
    parser.add_argument('-f', '--farm', type=str, help='desired Farm/Stack')
    parser.add_argument('-t', '--type', type=str, required=True, help='desired EC2 instance types')
    args = parser.parse_args()

    output = []
    output.append(args.region)
    output.append(args.farm)
    output.append(args.type)
    return output

def execute(target):
    print("\n\n")
    if target[1] is None:
        list_es = f'aws --profile prd ec2 describe-instances --region {target[0]} | grep -i "tam-{target[2]}"'
    else:
        list_es = f'aws --profile prd ec2 describe-instances --region {target[0]} | grep -i "tam-{target[2]}-{target[1]}"'
    os.system(list_es)
    print("\n\n")

execute(parse())
