from django.test import TestCase
from myapp.models import *

class TestCaseContact(TestCase):
    def setUp(self):
        contact_me.objects.create(
        name_field = "abdi",
        email_field = "mymail@mail.com",
        message_text = "words of importance")
        contact_me.objects.create(
        name_field = "testDummy",
        email_field = "mymail23@mail.com",
        message_text = "words of importance2")

    def test_contact_me_modal(self):
        """Model objects can be indentified"""
        abdi = contact_me.objects.get(name="abdi")
        testDummy = contact_me.objects.get(name="testDummy")
        self.assertTrue(abdi)
        self.assertTrue(testDummy)
