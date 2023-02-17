import random
import string
import sys

# variable
def string_generator(size=12, string=string.ascii_letters + string.digits):    
        return ''.join(random.choice(string) for _ in range(size))

#department
dept = input("Enter one selected department (from Marketing, Accounting, FinOps) : ")
if dept == "Marketing" :
    print ("you have selected department: ",dept)
elif dept == "Accounting" :
    print ("you have selected department: ",dept)
elif dept == "FinOps" :
    print ("you have selected department: ",dept)
else:
    print ("you should only select department from given options.")
    sys.exit()

#input from user on how many ec2 is required to be created.
ec2num = int(input("how many ec2 names would you like to be generated? "))

if ec2num > 0:
    print ("you have selected " + str(ec2num) + "ec2 names to be generated. ")

else:
    print ("you must select atleast 1 ec2 to be created.")

#informing using that automatically generating ec2 names
print ("now creating ec2 names based on your input")
print ()

for _ in range (1, ec2num + 1):
    ec2_name = dept + "_" + string_generator()
    print("your ec2 name : ",ec2_name)
