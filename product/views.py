from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product,Book,Category
from .serializers import ProductSerializer,BookSerializer,CategorySerializer,UserSerializer
from  rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.



@api_view(['GET'])
def get_books(request):
    query_set = Book.objects.all()
    serializer = BookSerializer(query_set,many=True)
    return Response({'status': 200, 'data': serializer.data})

    
class RegisterUser(APIView):     
     def post(self, request):
         serializer = UserSerializer(data=request.data )
         if not serializer.is_valid():
           return Response({'status': 403, 'message': serializer.errors})
         serializer.save()
         user = User.objects.get(username=serializer.data['username'])
         refresh = RefreshToken.for_user(user)
         return Response({'status': 200, 'data': {'refresh': str(refresh),'aacess':str(refresh.access_token)},'payload': serializer.data})
           

class ProductAPI(APIView):
     authentication_classes = [JWTAuthentication]
     permission_classes = [IsAuthenticated]
     
     def get(self, request):
          id=request.GET.get('id',None) 
          print(request.user)
          if id is None:
               product_objs = Product.objects.all()
               serializer = ProductSerializer(product_objs,many=True)
               return Response({'status': 200, 'data': serializer.data})
          try:     
              product_objs = Product.objects.get(id=id)
              serializer = ProductSerializer(product_objs)
              return Response({'status': 200, 'data': serializer.data})
          except Exception as e:   
             return  Response({'status': 403, 'message': 'Id invalid'})
              
              

         
     def post(self, request):
          data = request.data
          serializer = ProductSerializer(data=data)
          if not serializer.is_valid():
           return Response({'status': 403, 'message': serializer.errors})
          serializer.save()
          return Response({'status': 200, 'data': data})
        
     def put(self, request):
          try:
            id=request.GET.get('id') 
            product_objs = Product.objects.get(id=id)
            data = request.data
            serializer = ProductSerializer(product_objs,data=data)
            if not serializer.is_valid():
             return Response({'status': 403, 'message': serializer.errors})
            serializer.save()
            return Response({'status': 200, 'data': data,'message':'data update successful'}) 
          except Exception as e:   
           return  Response({'status': 403, 'message': 'Id invalid'})
         
     def patch(self, request):
        try:
            id=request.GET.get('id') 
            print('********************************',id)
            product_objs = Product.objects.get(id=id)
            data = request.data
            serializer = ProductSerializer(product_objs, data=data , partial=True)
            if not serializer.is_valid():
                return Response({'status': 403, 'message': serializer.errors})
            serializer.save()
            return Response({'status': 200, 'data': data,'message':'data update successful'}) 
        except Exception as e:   
            print(e)
            return  Response({'status': 403, 'message': 'Id invalid'})
         
     def delete(self, request):
        try:
           id=request.GET.get('id') 
           product_objs= Product.objects.get(id=id)
           product_objs.delete()
           return Response({'status': 200, 'message':'product delete successful'})
        except Exception as e: 
          print(e)
          return  Response({'status': 403, 'message': 'Id invalid'})














@api_view(['POST'])
def add_product(request):
    data = request.data
    serializer = ProductSerializer(data=data)
    if not serializer.is_valid():
        return Response({'status': 403, 'message': serializer.errors})
    serializer.save()
    return Response({'status': 200, 'data': data})

'''
@api_view(['GET'])
def product(request,id):
    queryset = Product.objects.get(id=id) 
    serializer = ProductSerializer(queryset)
    return Response({'status': 200, 'data': serializer.data})
'''

#Query parameters
@api_view(['GET'])
def product(request):
    try:
        id=request.GET.get('id')
        queryset = Product.objects.get(id=id) 
        serializer = ProductSerializer(queryset)
        return Response({'status': 200, 'data': serializer.data})
    except Exception as e: 
        print(e)
        return  Response({'status': 403, 'message': 'Id invalid'})



@api_view(['GET'])
def products(request):
    product_objs = Product.objects.all()
    serializer = ProductSerializer(product_objs,many=True)
    return Response({'status': 200, 'data': serializer.data})


@api_view(['PUT'])
def update_product(request,id):
    try:
        product_objs = Product.objects.get(id=id)
        data = request.data
        serializer = ProductSerializer(product_objs,data=data)
        if not serializer.is_valid():
            return Response({'status': 403, 'message': serializer.errors})
        serializer.save()
        return Response({'status': 200, 'data': data,'message':'data update successful'}) 
    except Exception as e:   
        return  Response({'status': 403, 'message': 'Id invalid'})
    
    
@api_view(['PATCH'])
def update_product(request,id):
    try:
        product_objs = Product.objects.get(id=id)
        data = request.data
        serializer = ProductSerializer(product_objs,data=data,partial=True)
        if not serializer.is_valid():
            return Response({'status': 403, 'message': serializer.errors})
        serializer.save()
        return Response({'status': 200, 'data': data,'message':'data update successful'}) 
    except Exception as e:   
        print(e)
        return  Response({'status': 403, 'message': 'Id invalid'})
    
    
@api_view(['DELETE'])    
def delete_product(request,id):    
    try:
      product_objs= Product.objects.get(id=id)
      product_objs.delete()
      return Response({'status': 200, 'message':'product delete successful'})
    except Exception as e: 
        print(e)
        return  Response({'status': 403, 'message': 'Id invalid'})