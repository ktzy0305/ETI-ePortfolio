from django.test import TestCase
from home.models import ContactMessage
# Create your tests here.

class HomeTest(TestCase):
    def test_submit_valid_contact_message(self):
        contact_message = ContactMessage(sender_name="Jack", sender_email="jack20@mail.com", message="Hi, can we meet up?")
        contact_message.save()
        latest_contact_message = ContactMessage.objects.latest("created_on")
        assert latest_contact_message.message == contact_message.message
