import subprocess
import boto3
import os
import datetime

now = datetime.datetime.now()

print("=====Starting Server Check=====")
print("Time: {}".format(now))
cmd = subprocess.Popen(['sudo', 'service', 'factorio', 'players-online'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = cmd.communicate()

output = output.decode().strip()

ec2 = boto3.client('ec2')

os.system("aws s3 sync /opt/factorio/saves s3://ryan-factorio-bucket/saves")
print("Synced")

if output:
    print("Players Online:")
    print(output)
else:
    ec2.stop_instances(InstanceIds=['i-0cd692cb7106be2b9'])
    print("Stopping Instance at {}".format(now))
print("=====Ending Server Check=====")
