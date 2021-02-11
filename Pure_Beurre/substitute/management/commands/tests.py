from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    print("Préparation de la campagne de tests")
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Lancement de la campagne de tests..."))
        subprocess.call([r'start_test.bat'])
        self.stdout.write(self.style.SUCCESS("Fin de la campagne de tests..."))
