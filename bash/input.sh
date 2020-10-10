#!/bin/bash

s="ec2"
r="us-east-1"

list=$(aws $s describe-instances   --region=$r --query 'Reservations[*].Instances[*].{id: InstanceId,state: State.Name}[]' )
#list1=($list)
echo $list |jq -pip install boto3