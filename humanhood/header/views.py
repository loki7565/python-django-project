from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def header(request):
  template = loader.get_template('header_page.html')
  return HttpResponse(template.render())