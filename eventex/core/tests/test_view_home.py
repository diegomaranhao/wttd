from django.shortcuts import resolve_url as r
from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """Get / must return status 200."""
        self.assertEqual(200, self.response.status_code)

    def test_template_index(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        url = r('subscriptions:inscricao')
        self.assertContains(self.response, f'href="{url}"')

    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'Alan Turing',
            'http://hbn.link/turing-pic'
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        url = r('home')
        expected = f'href="{url}#speakers"'
        self.assertContains(self.response, expected)