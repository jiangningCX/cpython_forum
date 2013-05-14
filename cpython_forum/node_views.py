#coding=utf-8
from django.http import HttpResponse
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from cpython_forum.models import *
from cpython_forum.forms import *

def nodecate_add (request):
	nodecates   = NodeCategory.objects.all()
	return render_to_response("nodecate_add.html",{'name':request.user.username,
            "nodecates":nodecates},context_instance=RequestContext(request))

def nodecate_save(request):

	if request.method == 'POST':
		nodecate = NodeCategory(name=request.POST['name'],description=request.POST['description'])
		nodecate.save()
		return  HttpResponseRedirect('/')	

def node_add (request,id):
	nodes      = Node.objects.filter(nodecate_id=id)
	nodecate   = NodeCategory.objects.get(id=id)
	return render_to_response("node_add.html",{'name':request.user.username,
            "nodes":nodes,'nodecate':nodecate},context_instance=RequestContext(request))

def node_save(request):

	if request.method == 'POST':
		nodecate = NodeCategory(name=request.POST['name'],description=request.POST['description'])
		nodecate.save()
		return  HttpResponseRedirect('/')		

def topic_add(request):
	articles = Article.objects.all()
	return render_to_response("node_article.html",{'name':request.user.username,'articles':articles},context_instance=RequestContext(request))

def topic_save(request):
	if request.method == 'POST':
                article = Article(title=request.POST['title'],content=request.POST['content'],user=request.user.username,username_id = request.user.id)
                article.save()
                return HttpResponseRedirect("/")
