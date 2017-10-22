import os
import getpass
import subprocess
from crontab import CronTab

def cronSetup():
    local_user = getpass.getuser()

    cron_file = CronTab(local_user)
   
def readConfig():
    pass

def cloneRepo(url, branch, path):
    # TODO replace this with the pygit library thing
    subprocess.call("git clone -b {branch} {url} {path}".format(**vars()), stdout=False)
  
def YNPrompt(question):
    yes = ["yes", "ye", "y", "yup", "yeah"]
    no = ["no", "n", "nope", "nah"]
    
    promt = question + " [Y/n] "

    while True:
        answer = (input(promt)).lower()
        if answer in yes:
            return True
        elif answer in no:
            return False
        else:
            print("Please answer yes or no")

