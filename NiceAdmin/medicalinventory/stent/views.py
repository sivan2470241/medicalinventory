from django.shortcuts import render
from django.http import HttpResponse
from .models import process_queue
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import MyModelSerializer
import requests
from django.http import JsonResponse



class medical_create(CreateView):
    model = process_queue
    fields = ['process_id','title','process_file_location','process_status','return_status','return_json','call_back_url','call_back_status','call_back_json','process_entry_date']
    template_name = "medical/create.html"
    success_url =reverse_lazy('listjournel')



class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = process_queue.objects.all()
    serializer_class = MyModelSerializer



def get_api_data(request):
    api_url = 'http://127.0.0.1:8000/api/'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
       
    else:
        return JsonResponse({'error': 'API request failed'}, status=500)
