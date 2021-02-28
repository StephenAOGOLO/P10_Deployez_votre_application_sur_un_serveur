from django.core.management import call_command
from pathlib import Path
import time, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def cyclic_dbupdate():
    try:
        now = time.localtime()
        when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
        start_time = when_happens
        print("Lancement de la mise à jour cyclique de la base de données...")
        print("Opération lancée à : {}".format(when_happens))
        call_command('fillDB')
        now = time.localtime()
        when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
        stop_time = when_happens
        print("Fin de la mise à jour cyclique de la base de données...")
        print("Opération terminée à : {}".format(when_happens))
        content = log_content(start_time, stop_time, "Mise a jour de la base de donnees")
        log_it(content=content)
    except Exception as e:
        print(e)


#def tests_dbupdate():
#    try:
#        cron_logger()
#        #print("Lancement de la mise à jour de la base de données...")
#        #call_command('fillDB')
#        #print("Fin de la mise à jour de la base de données...")
#    except Exception as e:
#        print(e)
#
#def cron_logger():
#    """
#    path_log = BASE_DIR + "/CRON_LOGS/"
#    name_log = "chronic_log"
#    extension = "txt"
#    now = time.localtime()
#    when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
#    content = ["cron task ==> " + when_happens, ]
#    #new_file = open(path_log+name_log+"_"+when_happens+"."+extension, "wt")
#    new_file = open(path_log+name_log+"."+extension, "wt")
#    for line in content:
#        new_file.write(line)
#    new_file.close
#    """
#    now = time.localtime()
#    when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
#    print("Tentative de création du dossier \n{} à {}".format(BASE_DIR + "/CRON_LOGS/", when_happens))
#    path_log = BASE_DIR + "/CRON_LOGS/"
#    os.mkdir(path_log)
#    print("Fin de tentative de création du dossier \n{} il est {}".format(BASE_DIR + "/CRON_LOGS/", when_happens))


def log_it(path_log="./CRON_LOGS/", filename="cron_event", extension="txt", content=None):
    if content is None:
        content = ["vide\n"]
    os.makedirs(path_log, exist_ok=True)
    now = time.localtime()
    when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
    creation_time = when_happens + "_"
    print("=" * 150)
    new_file = open(path_log + creation_time + filename+"."+extension, "wt")
    for ligne in content:
        new_file.write(ligne)
    new_file.close
    print("le fichier '{}.{}' est prêt".format(filename,extension))


def log_content(start_time, stop_time, event):
    event += "\n"
    return [start_time + " : Debut de " + event, stop_time + " : Fin de " + event]
