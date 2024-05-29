import json
from django.shortcuts import render,redirect
from django.views import View
# from django.http import HttpResponse
from django.template import loader
from .models import *
from rest_framework.throttling import UserRateThrottle
from .serializers import *
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
# from .forms import BookForm
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.views import exception_handler, APIView
from rest_framework.exceptions import APIException
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import mixins, generics
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend




class OncePerDayUserThrottle(UserRateThrottle):
  rate = '10/day'

# Create your views here.
@api_view(http_method_names=["POST"])
def content(request):
  if request.method == "POST":
    serilaizer= Serial2(data = request.data)
    if serilaizer.is_valid():
      serilaizer.save()
      return Response({"data":serilaizer.data}, status=status.HTTP_201_CREATED)
    else:
      return Response({'message': 'Error', "data": serilaizer.errors}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET","PATCH"])
class BookUpdate(APIView):
  def get(self,request,id):
    try:
      book = Book2.objects.get(pk=id)
    except Book2.DoesNotExist: 
      return Response({"Error": "Book Not Found"}, status=404)
    serializer=Serial(book)
    return Response({"data":serializer.data}, status=200)

  def patch(self, request, id):
    try:
      book = Book2.objects.get(pk=id)
    except Book2.DoesNotExist: 
      return Response({"Error": "Book Not Found"}, status=404)
    serializer=Serial(book, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response({"data":serializer.data}, status=201)
    
@api_view(["GET","PATCH"])
def updatebook(request, id):
  if request.method == "PATCH":
    try:
      book = Book2.objects.get(pk=id)
    except Book2.DoesNotExist: 
      return Response({"Error": "Book Not Found"}, status=404) 
    serializer=Serial(book, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response({"data":serializer.data}, status=201)

  if request.method == "GET":
    try:
      book = Book2.objects.get(pk=id)
    except Book2.DoesNotExist: 
      return Response({"Error": "Book Not Found"}, status=404)
    serializer=Serial(book)
    return Response({"data":serializer.data}, status=200)
  
@api_view(http_method_names=["POST", "GET"])
@throttle_classes([OncePerDayUserThrottle])
def formview(request:Request):

  if request.method == "POST":
    serializer = Serial(data = request.data)
    # data = json.loads(request.data) 
    # raise APIException(BadRequest)

    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response({'message': 'Created', "data": serializer.data}, status=status.HTTP_201_CREATED)
    # else:
    #   return Response({'message': 'Error', "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)      
  else:
    # context = {'BookData': Book2.objects.all(), 'form' : BookForm()}
    Bookdata = Book2.objects.all()
    serializers  = Serial(Bookdata,many=True)
    return Response({'message': 'Get Data', "books":serializers.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def home(request:Request):
  book = {'book_list': Book2.objects.all(), 'price': 150}
  # serial = Auth
  return render(request, 'home.html', book)


# @api_view(["GET"])
# def get_author_view(request, id):
#   book = Book2.objects.get(pk=id)
#   serializer=Serial(book)
#   return Response(serializer.data)

# class Authorview(APIView):
#   def get(self, request, id):
#     authordata1 = Author.objects.get(pk=id)
#     serializer  = Author_Serial(authordata1)
#     return Response(serializer.data, status=200)
  
#   def patch(self, request, id):
#     authordata1 = Author.objects.get(pk=id)
#     serializer  = Author_Serial(authordata1,data=request.data,partial=True)
#     if serializer.is_valid(raise_exception=True):
#       serializer.save()
#       return Response({'message': 'Created', "data": serializer.data}, status=status.HTTP_201_CREATED)

#   def put(self, request, id):
#     authordata1 = Author.objects.get(pk=id)
#     serializer  = Author_Serial(authordata1,data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       serializer.save()
#       return Response({'message': 'Created', "data": serializer.data}, status=status.HTTP_201_CREATED)

class Authorview(generics.RetrieveUpdateDestroyAPIView):
  queryset=Author.objects.all()
  serializer_class=Author_Serial
  # lookup_field='id'

# class Authorview(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#   queryset=Author.objects.all()
#   serializer_class=Author_Serial
  
#   def get(self, request, *args, **kwargs):
#     return self.retrieve(request, *args, **kwargs)
  
#   def patch(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)

# class Authorlist(APIView):
#   # authentication_classes=[SessionAuthentication]
#   # permission_classes=[IsAuthenticated]
  
#   def get(self, request):
#     authordata = Author.objects.all()
#     serializer  = Author_Serial(authordata, many=True, context={'request':request})
#     return Response(serializer.data, status=200)
  
#   def post(self, request):
#     # authordata1 = Author.objects.all()
#     serializer  = Author_Serial(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       serializer.save()
#       return Response({'message': 'Created', "data": serializer.data}, status=status.HTTP_201_CREATED)
    
# class Authorlist(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#   queryset=Author.objects.all()
#   serializer_class=Author_Serial
  
#   def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)
  
#   def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)
  
class AuthorList(generics.ListCreateAPIView):
  queryset=Author.objects.all()
  serializer_class=Author_Serial
  authentication_classes=[JWTAuthentication]
  permission_classes=[IsAuthenticated]
  # filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
  filterset_fields=['followers', 'firstname', 'lastname']
  ordering_fields=[ 'firstname', 'id']
  search_fields = ['^firstname']

# def testing(request):
#   context = {
#     'cars': [
#       {
#         'brand': 'Ford',
#         'model': 'Mustang',
#         'year': '1964',
#       },
#       {
#         'brand': 'Ford',
#         'model': 'Bronco',
#         'year': '1970',
#       },
#       {
#         'brand': 'Ford',
#         'model': 'Sierra',
#         'year': '1981',
#       },
#       {
#         'brand': 'Volvo',
#         'model': 'XC90',
#         'year': '2016',
#       },
#       {
#         'brand': 'Volvo',
#         'model': 'P1800',
#         'year': '1964',
#       }]
#     }
#   return render(request, 'home.html', context) 