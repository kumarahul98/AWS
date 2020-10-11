import boto3
import jmespath
from prettytable import PrettyTable
import time

def getEc2(region):
    #Connection
    global ec2 
    ec2 = boto3.client('ec2',region_name=region)
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

        print(x)
        print("Note: Enter -1 to exit or anyother key to refresh.")
        select=int(input("Select the VM-Number: "))
        if (select<=-1): 
            print("Exiting")
            return 1
        elif (select < counter):
            toggleState(instances[select-1][2],instances[select-1][3])
        else :
            continue

def toggleState(id, state):
    if(state=='running'):
        print("Press 1 to stop the instance(%s): " % id)
        op=int(input())
        if (op == 1):
            print("Stopping the instance..............\n\n")
            ec2.stop_instances(InstanceIds=[id])
        else :
            print("Canceling Operation!!!\n")
            return
    elif (state=='stopped'):
        print("Press 1 to start the instance(%s): " % id)
        op=int(input())
        if (op == 1):
            print("Starting the instance..............\n\n")
            ec2.start_instances(InstanceIds=[id])
        else :
            print("Canceling Operation!!!\n")
            return
    else :
        print("Wait for the VM to start or stop!!!\n\n")
    time.sleep(1)



