import subprocess
import os
from sys import platform, exit


if platform != "linux" or platform != "linux2":
    print(f"Oops you might need to install docker desktop your system is not running on linux but on {platform}")
else:
    os.chmod('./spin-up-app.sh', 0o755)
    rc = subprocess.call("./spin-up-app.sh")


with open("output.log", "a") as output:
    subprocess.call("git clone https://github.com/Bash-mocart/gbh-app.git", shell=True, stdout=output, stderr=output)
    subprocess.call("cd gbh-app && npm i", shell=True, stdout=output, stderr=output)
    subprocess.call("git clone https://github.com/Bash-mocart/gbh-api.git", shell=True, stdout=output, stderr=output)
    subprocess.call("cd gbh-api && npm i", shell=True, stdout=output, stderr=output)
    subprocess.call("docker-compose up", shell=True, stdout=output, stderr=output)



    


