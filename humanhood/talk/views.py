from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def talk(request):
  template = loader.get_template('talk_pages.html')
  return HttpResponse(template.render())
