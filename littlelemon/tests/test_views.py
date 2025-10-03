from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setup(self):
        self.item1 = Menu.objects.create(title="Pasta", price=12.50, inventory=10)
        self.item2 = Menu.objects.create(title="Pizza", price=15.00, inventory=5)
        self.item3 = Menu.objects.create(title="Salad", price=8.00, inventory=20)
        self.client = APIClient()

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menuitems = Menu.objects.all()
        serializer = MenuSerializer(menuitems, many=True)
        self.assertEqual(response.data, serializer.data)
