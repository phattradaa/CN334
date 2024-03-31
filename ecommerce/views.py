from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

# Create your views here.

def ecommerce_index_view(request):
    '''This function render index page of ecommerc views'''
    
    return HttpResponse('Welcome to 6410742099 Phattrada Mikota views')

def item_view(request, item_id):
    
    context_data = {
        "item_id" : item_id
    }
    
    return render(request,'index.html',context=context_data)

@csrf_exempt
def basic_request(request):
    if request.method == "GET":
        return JsonResponse({"status":"GET Pass"},safe=False)
    
    if request.method == "POST":
        return JsonResponse({"status":"POST pass"},safe=False)

@csrf_exempt
def tokenize(request):
    if request.method == "POST":
        try:
            sentence = request.POST['text']
        except:
            return JsonResponse({"error":"Input not found"},safe=False, status=500)
        url = "https://api.aiforthai.in.th/tlexplus"
        data = {'text':sentence}
        headers = {
            'Apikey' :"7Nnz7YqING7Q3LMriW4O4ph8VTK6I6aH"
        }     
        response = requests.post(url, data=data, headers=headers)
        response_json = response.json()
        return JsonResponse({"student":"student_id","tokenize":response_json},safe=False)
    
    return JsonResponse({"error":"Method not allowed"}, safe=False, status=403)

@csrf_exempt
def sentimental(request):
    if request.method == "POST":
        try:
            sentence = request.POST['text']
        except:
            return JsonResponse({"error":"Input not found"},safe=False, status=500)
        url = "https://api.aiforthai.in.th/ssense"
        data = {'text':sentence}
        headers = {
            'Apikey' :"7Nnz7YqING7Q3LMriW4O4ph8VTK6I6aH"
        }     
        response = requests.post(url, data=data, headers=headers)
        response_json = response.json()
        return JsonResponse({"student":"6410742099","sentiment":response_json},safe=False)
    
    return JsonResponse({"error":"Method not allowed"}, safe=False, status=403)
           
@csrf_exempt
def text2speech(request):
    if request.method == "POST":
        try:
            text = request.POST['text']
        except:
            return JsonResponse({"error":"Input not found"},safe=False, status=500)
        url = "https://api.aiforthai.in.th/vaja9/synth_audiovisual"
        data = {'input_text':text,'speaker': 1, 'phrase_break':0, 'audiovisual':0}
        headers = {
            'Apikey' :"7Nnz7YqING7Q3LMriW4O4ph8VTK6I6aH"
        }     
        response = requests.post(url, json=data, headers=headers)
        response_json = response.json()
        print(response_json)
        #response_dict = json.loads(response)
        return JsonResponse({"student":"6410742099","output":response_json['wav_url']},safe=False)
    
    return JsonResponse({"error":"Method not allowed"}, safe=False, status=403)
             