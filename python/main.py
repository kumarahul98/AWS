import ec2
import rds

select=1
region='us-east-1'
while select:
    print("1. EC2 \n2. RDS ")
    select=int(input("Select the Service: "))
    if (select<=-1): 
        print("Exitting")
        exit(0)
    elif (select==1):
        ec2.getEc2(region)
    elif (select==2):
        rds.getRds(region)
    else :
        continue
