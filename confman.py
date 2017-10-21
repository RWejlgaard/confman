import os
import getpass
from crontab import CronTab

def cronSetup():
    localUser = getpass.getuser()

    cronFile = CronTab(user=localUser)
    
def readConfig()



