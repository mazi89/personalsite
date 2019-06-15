import os
import mailbox
from .models import Inbox
mbox = mailbox.Maildir('~/Maildir/new')

for message in mbox:
    if message.is_multipart():
        content = ''.join([part.get_payload(decode=True) for part in message.get_payload()])
    else:
        content = message.get_payload(decode=True).as_string()
    Inbox.create(
    delivered_to=message['Delivered-To'],
    email_from=message['From'],
    subject_field=message['Subject'],
    message_body=content,
    date_received=message['Received'],
    )
    print('New message received')
