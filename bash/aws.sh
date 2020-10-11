#!/bin/sh

echo "What's your region"
read Region
echo "Specify Service Name"
read Service
InstanceId="i-041057f9fade3a43f"
while :
do
aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,State.Name,Tags[?Key==`Name`].Value[]]' --region $Region --output text
echo "Select instance id to change its state"
read InstanceId
if [[ $InstanceId == "-1" ]]
 then
    break
fi
for i in $InstanceId
do
echo $i
var=$(aws ec2 describe-instances --instance-ids $i --query 'Reservations[].Instances[].[State.Name]' --output text)
if [[ $var == "running" ]]
then
echo "Stopping"
aws ec2 stop-instances --instance-ids $i > /dev/null
elif [[ $var == "stopped" ]]
then
echo "Starting"
aws ec2 start-instances --instance-ids $i > /dev/null
else
echo "its in pending state"
fi
done
done

