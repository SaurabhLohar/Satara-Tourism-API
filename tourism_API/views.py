from django.shortcuts import render
from rest_framework import generics
from .serializers import PlacesSerializer

from django.http import JsonResponse,HttpResponse


from rest_framework import permissions
from rest_framework import mixins

from .models import Place
# Create your views here.

from rest_framework import status
from rest_framework.response import Response

def index(request):
	return render(request,'index.html')

class Places(generics.GenericAPIView,
	mixins.ListModelMixin,
	mixins.CreateModelMixin,
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	serializer_class = PlacesSerializer
	queryset = Place.objects.all()

	lookup_field = 'id'
	
	def get(self,request,id=None):
		if id:
			return self.retrieve(request)
		else:
			return self.list(request)

	def post(self,request):
		return self.create(request)

	def put(self,request,id):
		return self.update(request,id)


def custom404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'please move along': 'nothing to see here',
    })

def custom500(request):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    })