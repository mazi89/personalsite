#!/sites/abdinasirnoor.com/.venv/bin/python3.6
import sys, os, mailbox
sys.path.append('/sites/abdinasirnoor.com/src/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personalsite.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = 'personalsite.settings'
import django
django.setup()
from django.conf import settings
from django.core.management.base import BaseCommand
from landingpage.models import Inbox
from datetime import datetime

class Command(BaseCommand):
    help = 'send email notification'

    def handle(self, *args, **options):
        mbox = mailbox.Maildir('/home/abdinasir/Maildir/')
        for message in mbox:
            message_object = Inbox.objects.filter(message_id=message['Message-ID']).exists()
            if (message_object == False):
                if message.is_multipart():
                    content = ''.join([part.as_string() for part in message.get_payload()])
                else:
                    content = str(message.get_payload(decode=True))
                #remove comma and paranthesis around time zone causes format error
                date_cleaned = message['Date']
                date_cleaned = date_cleaned.translate(str.maketrans({',': '', '(': '', ')': '',}))
                inbox_object = Inbox(
                message_id=message['Message-ID'],
                delivered_to=message['Delivered-To'],
                email_from=message['From'],
                subject_field=message['Subject'],
                message_body=content,
                original_date=datetime.strptime(date_cleaned, '%a %d %b %Y %H:%M:%S %z %Z'),
                )
                inbox_object.save()
                self.stdout.write(self.style.SUCCESS('Successfully added messages!'))
        self.stdout.write(self.style.SUCCESS('Messages added! Shutting down....'))
