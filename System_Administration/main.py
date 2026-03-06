import subprocess



pem_file = "/c/Users/Lenovo/OneDrive/Backup_23102024/d_drive/PERSONAL/Career/Projects/Beginner_Projects/labsuser.pem"
ec2_user = "ec2-user"
ec2_public_ip = "54.188.162.118"
new_user = "sujay2"
remote_command = f"ls -la /home/{new_user}"


#check if the user exists, 
check_user = subprocess.run([
    "ssh",
    "-i", pem_file,
    f"{ec2_user}@{ec2_public_ip}",
    remote_command
])

#if returncode is not 0, creates the user
if check_user.returncode!=0:
    print ("user does not exist! you can add a new user")
    subprocess.run ([
        "ssh",
        "-i", pem_file,
        f"{ec2_user}@{ec2_public_ip}",
        f"sudo useradd -m {new_user}"
    ])
else:
    print ("user already exists")








