from django.shortcuts import render
from rest_framework.views import APIView
from .models import brand, product, Seller, order, filemodel
from .serializers import fileserializer , brandserializer
from rest_framework.response import Response
from .file_folder import file_data
from django.conf import settings
from rest_framework import viewsets
from .rate_limiter import rate_limit
# Create your views here.


class fileview(APIView):
    
    def post(self, request):
        try :
            data = request.data
            print(data)
            # file_data()
            serializer = fileserializer(data= data)
            if serializer.is_valid():
                serializer.save()
                filepath = (serializer.data['file'])
                file_data(f"{settings.BASE_DIR}/{filepath}")
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
class brandsview(viewsets.ModelViewSet):
    queryset = brand.objects.all()
    serializer_class = brandserializer
    
    @rate_limit(max_requests=5, time_period=60)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)