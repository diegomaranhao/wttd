from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()


    def test_form_has_fields(self):
        """Form must have four fields"""
        expect = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expect, list(self.form.fields))