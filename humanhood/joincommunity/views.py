from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def joincommunity(request):
  template = loader.get_template('join_our_community.html')
  return HttpResponse(template.render())