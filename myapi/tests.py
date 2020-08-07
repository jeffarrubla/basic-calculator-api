import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

#initialize the APIClient app
client = Client()

class SumTest(TestCase):
	""" Test module for the sum API """

	def test_sum(self):
		# get API response
		response = client.get(reverse('sum', kwargs={'a':1,'b':2}))
		# do assertions
		self.assertEqual(response.json()['result'], 3)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_bad_sum(self):
		# get API response
		response = client.get(reverse('sum', kwargs={'a':1,'b':'s'}))
		# do assertions
		self.assertEqual(response.json()['Error'],"could not convert string to float: 's'")

	def test_sum_symbol(self):
		#get API response
		response = client.get(reverse('sum', kwargs={'a':'+','b':100}))
		# do assertions
		self.assertEqual(response.json()['Error'],"could not convert string to float: '+'")

	def test_sum_float(self):
		# get API response
		response = client.get(reverse('sum', kwargs={'a':'30.334','b':100}))
		# do assertions
		self.assertEqual(response.json()['result'],130.334)