from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class PageTests(TestCase):

  ###############
  ## Home Page ##
  ###############

  def test_home_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_home_templates(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'home.html')
    self.assertTemplateUsed(response, 'nav.html')

  ##############
  ## About Us ##
  ##############

  def test_about_status_code(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_about_templates(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'about.html')
    self.assertTemplateUsed(response, 'nav.html')
