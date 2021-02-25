from django.core.management import call_command
from pathlib import Path
import time

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def weekly_dbupdate():
  pass


def tests_dbupdate():
    try:
        cron_logger()
        #print("Lancement de la mise à jour de la base de données...")
        #call_command('fillDB')
        #print("Fin de la mise à jour de la base de données...")
    except Exception as e:
        print(e)

def cron_logger():
    path_log = BASE_DIR + "/CRON_LOGS/"
    name_log = "chronic_log"
    extension = "txt"
    now = time.localtime()
    when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
    content = ["cron task ==> " + when_happens, ]
    #new_file = open(path_log+name_log+"_"+when_happens+"."+extension, "wt")
    new_file = open(path_log+name_log+"."+extension, "wt")
    for line in content:
        new_file.write(line)
    new_file.close