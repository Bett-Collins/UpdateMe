from django.test import TestCase

# Create your tests here.
class BusinessTestClass(TestCase):
    #setup method
    def setUp(self):
        self.business=Business(name='cereals',email="a@gmail.com")
