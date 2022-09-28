from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class AppTest(TestCase):
    def test_200_html(self):
        response = Client().get('/mywatchlist/html/', follow=True)
        self.assertEqual(response.status_code,200)

    def test_200_json(self):
        response = Client().get('/mywatchlist/json/', follow=True)
        self.assertEqual(response.status_code,200)

    def test_200_xml(self):
        response = Client().get('/mywatchlist/xml/', follow=True)
        self.assertEqual(response.status_code,200)
    
    def test_app_using_to_do_list_template(self): # not as essentials as the first three above
        response = Client().get('/mywatchlist/')
        self.assertTemplateUsed(response, 'mywatchlist.html')