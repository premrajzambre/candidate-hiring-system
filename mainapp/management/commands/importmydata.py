from mainapp.models import applicant
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        insert_count = applicant.objects.from_csv('/home/premraj/Documents/applications.csv')
        print ("{} records inserted").format(insert_count)
