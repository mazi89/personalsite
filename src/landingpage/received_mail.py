import sys, os, mailbox, django
from django.conf import settings
settings.configure(DEBUG=True)

from landingpage.models import Inbox
mbox = mailbox.Maildir('~/Maildir/new')

for message in mbox:
    if message.is_multipart():
        content = ''.join([part.get_payload(decode=True) for part in message.get_payload()])
    else:
        content = message.get_payload(decode=True).as_string()
    inbox_object = Inbox(
    delivered_to=message['Delivered-To'],
    email_from=message['From'],
    subject_field=message['Subject'],
    message_body=content,
    date_received=message['Received'],
    )
    inbox_object.save()
    print('New message received')
