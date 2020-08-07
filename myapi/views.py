from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.
@api_view(['GET'])
def index(request):
	return  JsonResponse({'message': 
		'This is a calculator, the functions are: '+
		'sum: /api/sum/num1/num2'})

@api_view(['GET'])
def sum(request,a,b):	
	if request.method == 'GET':
		a = int(a) if float(a).is_integer() else float(a)
		b = int(b) if float(b).is_integer() else float(b)
		return JsonResponse( {'result': a+b}, safe=False) 
	
	return JsonResponse({"Error": "Not method GET"}, status=status.HTTP_404_NOT_FOUND) 