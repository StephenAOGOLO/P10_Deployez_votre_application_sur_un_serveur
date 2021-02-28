from django.core.management.base import BaseCommand
from substitute.models import *

class Command(BaseCommand):
    print("Consultation des aliments de la base de donnees")

    def handle(self, *args, **options):
        quantity = len(Aliment.objects.all())
        self.stdout.write(self.style.SUCCESS("La base de donnees contient {} aliments".format(quantity)))