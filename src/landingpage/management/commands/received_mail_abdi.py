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

class Command(BaseCommand):
    help = 'send email notification'

    def handle(self, *args, **options):
        mbox = mailbox.Maildir('/home/abdinasir/Maildir/')
        for message in mbox:
            if message.is_multipart():
                content = ''.join([part.as_string() for part in message.get_payload()])
            else:
                content = str(message.get_payload(decode=True))
            inbox_object = Inbox(
            delivered_to=message['Delivered-To'],
            email_from=message['From'],
            subject_field=message['Subject'],
            message_body=content,
            date_received=message['Received'],
            )
            inbox_object.save()
        self.stdout.write(self.style.SUCCESS('Successfully added messages!'))
