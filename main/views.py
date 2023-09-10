from django.shortcuts import render, redirect
from django.http import HttpResponse
from .util import obfuscate_via_lsb, deobfuscate_via_lsb, make_attachment_response
import time

# Create your views here.
def home(request):
    return render(request, "cybercamo/index.html")

def about(request):
    return render(request, "cybercamo/about.html")

def embed(request):
    payload_file = request.FILES["payloadFile"]
    input_file = request.FILES["inputFile"]
    data = obfuscate_via_lsb(payload_file, input_file)
    if not data:
        return redirect("main_route")
    else:
        return make_attachment_response(data, f'cybercamo_{input_file.name}')
    
def extract(request):
    
    input_file = request.FILES["inputFile"]
    data = deobfuscate_via_lsb(input_file)
    if not data:
        return redirect("main_route")
    else:
        return make_attachment_response(data, "payload")