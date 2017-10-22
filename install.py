# import os
import sys
# import git
# import getpass
import confman
import subprocess
from crontab import CronTab

def install():
    dictInput = dict(enumerate(sys.argv))

    gitURL = dictInput.get(1) or showHelp()
    gitBranch = dictInput.get(2, "master")

    print("Repo URL = " + gitURL)
    print("Branch = " + gitBranch)
   
    if not YNPrompt("Is the following correct?"):
        exit()
    
    cloneRepo(gitURL, gitBranch, "/tmp/confman/dotfile_repo")
    


def cloneRepo(url, branch, path):
    # TODO replace this with the pygit library thing
    subprocess.call("git clone -b {branch} {url} {path}".format(**vars()), stdout=False)
     


def showHelp():
    print("Something went wrong")
    print("Please make sure you write the git url after install.py")
    print("Like so, 'python install.py [url] [branch]'")
    return exit()

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

if __name__ == "__main__":
    install()
