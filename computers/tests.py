from django.test import TestCase
from django.urls import reverse

from .models import Computer


class ComputerModelTests(TestCase):

    def test_was_out_of_stocks_with_positive_stock_number(self):
        """
        was_out_of_stocks() returns False for Computers whose stock
        is larger than zero
        """
        computer = Computer(stocks=10)
        self.assertIs(computer.was_out_of_stock(), False)

    def test_was_out_of_stocks_with_zero_stock_number(self):
        """
        was_out_of_stocks() returns True for Computers whose stock
        is equal to zero
        """
        computer = Computer(stocks=0)
        self.assertIs(computer.was_out_of_stock(), True)

    def test_was_out_of_stocks_with_negative_stock_number(self):
        """
        was_out_of_stocks() returns True for Computers whose stock
        is less than zero
        """
        computer = Computer(stocks=-3)
        self.assertIs(computer.was_out_of_stock(), True)


def create_computer(name, brand, picture, rent):
    """
    Create a computer with the given 'name', 'brand', 'picture'
    and 'rent'
    """
    return Computer.objects.create(name=name, brand=brand, picture=picture, rent=rent)


class ComputerHomeViewTests(TestCase):
    def test_no_computers(self):
        """
        If no computers exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('computers:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No computers are available.')
        self.assertQuerysetEqual(response.context['computer_list'], [])

    def test_exist_computers(self):
        """
        Computers exist and are displayed on the homepage
        """
        computer = create_computer('MacBook', 'Apple', 'http://google.com', 20)
        response = self.client.get(reverse('computers:home'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['computer_list'], [computer])
