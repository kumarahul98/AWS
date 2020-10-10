import boto3
from pprint import pprint
import jmespath
from prettytable import PrettyTable
    
#Connection
ec2 = boto3.client('ec2',region_name='us-east-1')


#Getting instance list
instances = ec2.describe_instances()

#jmespath
#pf1='Reservations[*].Instances[*].{InstanceId: InstanceId,state: State.Name,Name: Tags[?Key==`Name`]|[0].Value}[]'
pf1='Reservations[*].Instances[*].[Tags[?Key==`Name`]|[0].Value,InstanceId,State.Name][]'
pf2=jmespath.search(pf1,instances)
k=1
x = PrettyTable()
x.field_names = ["S.NO", "InstanceName", "InstanceId", "State"]
for i in pf2:
    i.insert(0,k)
    k+=1
    x.add_row(i)
    print(i)

print((x))

# pf=instances['Reservations']
# for i in pf:
#     pprint(i['Instances'][0]['InstanceId'])

# pprint(instances)
# for instance in instances:
#     print(instance.id, instance.instance_type)