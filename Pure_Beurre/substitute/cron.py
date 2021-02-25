from django.core.management import call_command
from pathlib import Path
import time, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def cyclic_dbupdate():
    try:
        now = time.localtime()
        when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
        print("Lancement de la mise à jour cyclique de la base de données...")
        print("Opération lancée à : {}".format(when_happens))
        call_command('fillDB')
        now = time.localtime()
        when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
        print("Fin de la mise à jour cyclique de la base de données...")
        print("Opération terminée à : {}".format(when_happens))
    except Exception as e:
        print(e)


def tests_dbupdate():
    try:
        cron_logger()
    except Exception as e:
        print(e)

def cron_logger():
    """
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
    """
    now = time.localtime()
    when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
    print("Tentative de création du dossier \n{} à {}".format(BASE_DIR + "/CRON_LOGS/", when_happens))
    path_log = BASE_DIR + "/CRON_LOGS/"
    os.mkdir(path_log)
    print("Fin de tentative de création du dossier \n{} il est {}".format(BASE_DIR + "/CRON_LOGS/", when_happens))