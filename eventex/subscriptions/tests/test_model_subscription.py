from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Diego Maranhão',
            cpf='12344321123',
            email='henrique@bastos.net',
            phone='69-020322323'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """An subscription must have a field that recorder when it was create"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual("Diego Maranhão", str(self.obj))

    def test_paid_default_to_False(self):
        """By defaul paid must be False"""
        self.assertEqual(False, self.obj.paid)