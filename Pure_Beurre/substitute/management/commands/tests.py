from django.core.management.base import BaseCommand
import subprocess, os

class Command(BaseCommand):
    print("Préparation de la campagne de tests")
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Lancement de la campagne de tests..."))
        try:
            shell_script()
        except Exception as e:
            print(e)
        self.stdout.write(self.style.SUCCESS("Fin de la campagne de tests..."))

def batch_script():
    subprocess.call([r'start_test.bat'])

def shell_script():
    subprocess.call([r'start_test.sh'])

def native_shell_script():
    os.system("coverage run --source='.' manage.py test substitute.project_tester.selenium substitute.project_tester.tests")
    os.system("coverage html --skip-covered --skip-empty -d substitute\project_tester\coverage_html")
    os.system("start substitute\project_tester\coverage_html\index.html")