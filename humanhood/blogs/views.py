from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def blogs(request):
  template = loader.get_template('blogs_page.html')
  return HttpResponse(template.render())