from django.test import TestCase
from django.shortcuts import resolve_url as r
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Diego Maranhão', cpf='12345678901', email='dom@eventos.com', phone='32-21234-2321')
        url = r('subscriptions:inscricao')
        self.response = self.client.post(url, data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'dom@eventos.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Diego Maranhão',
            '12345678901',
            'dom@eventos.com',
            '32-21234-2321',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
