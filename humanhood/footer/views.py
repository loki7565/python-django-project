from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def footer(request):
  template = loader.get_template('footer_page.html')
  return HttpResponse(template.render())