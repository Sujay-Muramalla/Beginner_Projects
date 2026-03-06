import subprocess



pem_file = "/c/Users/Lenovo/OneDrive/Backup_23102024/d_drive/PERSONAL/Career/Projects/Beginner_Projects/labsuser.pem"
ec2_user = "ec2-user"
ec2_public_ip = "54.188.162.118"
new_user = "sujay1"


check_user = subprocess.run([
    "ssh",
    "-i", pem_file,
    f"{ec2_user}@{ec2_public_ip}",
    f"id {new_user}"
])

subprocess.run ([
    "ssh",
    "-i", pem_file,
    f"{ec2_user}@{ec2_public_ip}",
    f"sudo useradd -m {new_user}"
])





