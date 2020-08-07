from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.
@api_view(['GET'])
def index(request):
	return  JsonResponse({'message': 
		'This is a calculator, the functions are => '+
		'sum',
		'sum': '/api/sum/num1/num2',
		'subs': '/api/subs/num1/num2',
		})

@api_view(['GET'])
def sum(request,a,b):	
	if request.method == 'GET':
		try:
			a = int(a) if float(a).is_integer() else float(a)
			b = int(b) if float(b).is_integer() else float(b)		
			return JsonResponse( {'result': a+b}, status=status.HTTP_200_OK,safe=False) 
		except ValueError as e:					
			return JsonResponse({"Error":str(e)}, status=status.HTTP_400_BAD_REQUEST) 
		except:			
			return JsonResponse({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST) 	
			
	return JsonResponse({"Error": "Not method GET"}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def subt(request,a,b):	
	if request.method == 'GET':
		try:
			a = int(a) if float(a).is_integer() else float(a)
			b = int(b) if float(b).is_integer() else float(b)
			return JsonResponse( {'result': round(a-b,4)}, status=status.HTTP_200_OK, safe=False) 
		except ValueError as e:					
			return JsonResponse({"Error":str(e)}, status=status.HTTP_400_BAD_REQUEST) 
		except:			
			return JsonResponse({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST) 	

	return JsonResponse({"Error": "Not method GET"}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def mul(request,a,b):
	if request.method == 'GET':
		try:
			a = int(a) if float(a).is_integer() else float(a)
			b = int(b) if float(b).is_integer() else float(b)
			return JsonResponse( {'result': round(a*b,6)}, status=status.HTTP_200_OK, safe=False) 
		except ValueError as e:					
			return JsonResponse({"Error":str(e)}, status=status.HTTP_400_BAD_REQUEST) 
		except:			
			return JsonResponse({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST) 	

	return JsonResponse({"Error": "Not method GET"}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def div(request,a,b):
	if request.method == 'GET':
		a = int(a) if float(a).is_integer() else float(a)
		b = int(b) if float(b).is_integer() else float(b)
		return JsonResponse( {'result': a/b,'module':a%b }, status=status.HTTP_200_OK, safe=False) 

	return JsonResponse({"Error": "Not method GET"}, status=status.HTTP_404_NOT_FOUND) 