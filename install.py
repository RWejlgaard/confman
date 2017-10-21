import os
import sys
import git
import getpass
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

    


def showHelp():
    print("Something went wrong")
    print("Please make sure you write the git url after install.py")
    print("Like so, 'python install.py [url] [branch]'")
    return exit()

def YNPrompt(question):
    yes = ["yes", "ye", "y"]
    no = ["no", "n"]
    
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
