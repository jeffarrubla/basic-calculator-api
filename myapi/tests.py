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
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_sum_symbol(self):
		#get API response
		response = client.get(reverse('sum', kwargs={'a':'+','b':100}))
		# do assertions
		self.assertEqual(response.json()['Error'],"could not convert string to float: '+'")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_sum_float(self):
		# get API response
		response = client.get(reverse('sum', kwargs={'a':'30.334','b':100}))
		# do assertions
		self.assertEqual(response.json()['result'],130.334)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class SubsTest(TestCase):
	""" Test module for substraction API """

	def test_subs(self):
		# get API response
		response = client.get(reverse('substraction',kwargs={'a': 4, 'b': 2}))
		# do assertions 
		self.assertEqual(response.json()['result'],2)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_subs_negative_result(self):
		# get API response
		response = client.get(reverse('substraction',kwargs={'a':'2','b':'3'}))
		# do assertions
		self.assertEqual(response.json()['result'],-1)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_subs_special_char(self):
		#get API response
		response = client.get(reverse('substraction',kwargs={'a':'s','b':5}))
		# do assertions
		self.assertEqual(response.json()['Error'],"could not convert string to float: 's'")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_subs_with_symbol(self):
		# get API response
		response = client.get(reverse('substraction',kwargs={'a':'-','b':'4'}))
		# do assertions
		self.assertEqual(response.json()['Error'],"could not convert string to float: '-'")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_sub_with_float(self):
		# get API response
		response = client.get(reverse('substraction',kwargs={'a':'10.5935','b':'1002.49'}))
		# do assertions
		self.assertEqual(response.json()['result'],-991.8965)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class MulTest(TestCase):
	""" Test module for multiplication API """

	def test_mul(self):
		# get API response
		response = client.get(reverse('multiplication',kwargs={'a':3,'b':4}))
		# do assertions
		self.assertEqual(response.json()['result'],12)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_mul_with_symbol(self):
		# get API response
		response = client.get(reverse('multiplication',kwargs={'a':'3','b':'*'}))
		# do assertions
		self.assertEqual(response.json()['Error'],"could not convert string to float: '*'")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_mul_with_float(self):
		#get API response
		response = client.get(reverse('multiplication',kwargs={'a':'30.405','b':'4003.2030'}))
		# do assertions
		self.assertEqual(response.json()['result'],121717.387215)
		self.assertEqual(response.status_code, status.HTTP_200_OK)