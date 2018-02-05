from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionsNewGet(TestCase):
    def setUp(self):
        url = r('subscriptions:inscricao')
        self.response = self.client.get(url)

    def test_get(self):
        """ Get /inscricao/ must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """ Html must contain input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_hast_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    


class SubscriptionsNewPost(TestCase):
    def setUp(self):
        data = dict(name='Diego Maranhão', cpf='12345678901', email='dom@eventos.com',
                    phone='32-21234-2321')
        url = r('subscriptions:inscricao')
        self.response = self.client.post(url, data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/<int:pk>/"""
        self.assertRedirects(self.response, r('subscriptions:inscricao-detalhada', 1))

    def test_send_subscribe_email(self):
        self.email = mail.outbox[0]
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionsNewPostInvalid(TestCase):
    def setUp(self):
        url = r('subscriptions:inscricao')
        self.response = self.client.post(url, {})

    def test_post(self):
        """Invalid post should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

