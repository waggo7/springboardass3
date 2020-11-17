from unittest import TestCase
from algorithms import reverse_str, is_palindrome, factorial
from arithemtic import adder
from app import app
from flask import session

# import pdb
# pdb.set_trace()


class ConversionTest(TestCase):
    def  test_home(self):
        with app.test_client() as client:
            res =client.get('/') #this dictates which function/method is going to be tested by its decorator
            html = res.get_data(as_text= True)

            self.assertEqual(res.status_code, 200)
        
    def test_inputs(self):
        with app.test_client() as client:
            res = client.get('/checkinputs')
            html = res.get_data(as_text = True)

            self.assertEquals(res.status_code,200)
            