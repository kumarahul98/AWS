import boto3
import jmespath
from prettytable import PrettyTable
import time

def getRds(region):
    #Connection
    global rds
    rds = boto3.client('rds',region_name=region)
    select=1
    while select:
        filter_string='DBInstances[].[DBInstanceIdentifier,DBInstanceStatus]'
        response = rds.describe_db_instances()
        instances=jmespath.search(filter_string,response)
        counter=1
        x = PrettyTable()
        x.field_names = ["S.NO", "RDSInstanceName", "State"]
        for instance in instances:
            instance.insert(0,counter)
            counter+=1
            x.add_row(instance)

        print(x)
        print("Note: Enter -1 to exit or anyother key to refresh.")
        select=int(input("Select the VM-Number: "))
        if (select<=-1): 
            print("Exiting..")
            return 1
        elif (select < counter):
            toggleState(instances[select-1][1],instances[select-1][2])
        else :
            continue

def toggleState(id, state):
    if(state=='available'):
        print("Press 1 to stop the instance(%s): " % id)
        op=int(input())
        if (op == 1):
            print("Stopping the instance..............")
            rds.stop_db_instance(DBInstanceIdentifier=id)
        else :
            print("Canceling Operation!!!\n")
            return
    elif (state=='stopped'):
        print("Press 1 to start the instance(%s): " % id)
        op=int(input())
        if (op == 1):
            print("Starting the instance..............")
            rds.start_db_instance(DBInstanceIdentifier=id)
        else :
            print("Canceling Operation!!!\n")
            return
    else :
        print("Wait for the VM to start or stop!!!")
    print("\nNote: Changing instance takes a few minutes!!!\n\n ")





