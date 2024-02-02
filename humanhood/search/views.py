from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def search(request):
  template = loader.get_template('search_page.html')
  return HttpResponse(template.render())