from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def purchase(request):
  template = loader.get_template('purchase_code.html')
  return HttpResponse(template.render())