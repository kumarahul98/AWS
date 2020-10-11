import boto3
import jmespath
from prettytable import PrettyTable
import time

def getInstances():
    select=1
    while select:
        #Getting instance list
        response = ec2.describe_instances()
        filter_string='Reservations[*].Instances[*].[Tags[?Key==`Name`]|[0].Value,InstanceId,State.Name][]'
        instances=jmespath.search(filter_string,response)
        counter=1
        x = PrettyTable()
        x.field_names = ["S.NO", "InstanceName", "InstanceId", "State"]
        for instance in instances:
            instance.insert(0,counter)
            counter+=1
            x.add_row(instance)

        print((x))
        print("Note: Enter -1 to exit or anyother key to refresh.")
        select=int(input("Select the VM-Number:"))
        if (select<=-1): 
            print("Exitting")
            exit(0)
        elif (select < counter):
            toggleState(instances[select-1][2],instances[select-1][3])
        else :
            continue

def toggleState(id, state):
    if(state=='running'):
        ec2.stop_instances(InstanceIds=[id])
    elif (state=='stopped'):
        ec2.start_instances(InstanceIds=[id])
    else :
        print("Wait for the VM to start or stop!!!")
    time.sleep(2)

#Connection
ec2 = boto3.client('ec2',region_name='us-east-1')

getInstances()