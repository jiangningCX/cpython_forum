#coding=utf-8
from django.http import HttpResponse
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from cpython_forum.models import *
from django.shortcuts import get_object_or_404
from cpython_forum.forms import *
import urllib

#from cpython_forum.forms import ProfileForm, RegisterForm
#import os

#from upload_avatar.cpython_forum_settings import (
#    UPLOAD_AVATAR_UPLOAD_ROOT,
#    UPLOAD_AVATAR_AVATAR_ROOT,
#    UPLOAD_AVATAR_RESIZE_SIZE,
#)

#from upload_avatar import get_uploadavatar_context

#from cpython_forum.models import User
def index_gegeda(request):
	
	articles    = Article.objects.all().order_by('-id')
	return render_to_response('index_gegeda.html',{'articles':articles},context_instance=RequestContext(request))

def index(request):
	topics      = Topic.objects.all()
	nodecates   = NodeCategory.objects.all()
	nodes	    = Node.objects.all()
	articles    = Article.objects.all().order_by('-id')
	for article in articles:
		print article.username_id

		img = Upload.objects.filter(user_id=article.username_id)

		for n in img:
			if img:
				image = n.image
			else:
				image = "static/media/gravatar.png"

			setattr(article,"image",image)
				
#	for article in articles:
#		sayss = says.objects.filter(sayid=article.id)
#		i = 0
#		for n in sayss:
#			i=i+1
	u_all = User.objects.all()
	names  = Celebrity.objects.all()
#	for user in names:
#		print user.name
#	for user_all in u_all:
#		print user_all.username
	image_urls   = Image.objects.get(pk=1)
	uploadimages = Upload.objects.filter(user_id=request.user.id)
	
	print uploadimages
	
	for uploadimage in uploadimages:
		print uploadimage
	#name   = Celebrity.objects.filter(user.id == request.user.username)
	#print name
#	for image_url in image_urls:
#		print image_url.image
	for n in nodecates:
		n.description = n.description[:5]+'.....'
	count = 0
	for n in articles:
		count = count+1
	#saycount = saycount()
	return render_to_response("index.html",{'name':request.user.username, 'topics':topics,"nodecates":nodecates,'articles':articles,'count':count,'image_urls':image_urls,'uploadimages':uploadimages},context_instance=RequestContext(request))

def register(request):
	form = UserCreationForm()
	if request.method == 'GET':
		return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
		return HttpResponseRedirect("/")

def node_index(request):
        topics      = Topic.objects.all()
        nodecates   = NodeCategory.objects.all()
        nodes       = Node.objects.all()
	topic      = Topic.objects.all()
        return render_to_response("node_index.html",{'name':request.user.username, 'topics':topics,\
            "nodecates":nodecates,"topic":topic},context_instance=RequestContext(request))

def say(request,offset):
	if request.user.is_authenticated():
		form = saysForm()
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		articles = Article.objects.get(id=offset)
		
		if request.method == 'POST':
			new_say = says(content = request.POST['content'],sayid=offset,user=request.user.username)
			new_say.save()
		saysss = says.objects.all()
		s = 0
		for n in saysss:
			s=s+1
		sayss = says.objects.filter(sayid = offset)
		i = 0
		for n in sayss:
			i = i+1
		return render_to_response("say.html",{"name":request.user.username,"articles":articles,"form":form,"says":sayss,"i":i,"s":s},context_instance=RequestContext(request))
	return render_to_response("say.html")

def delete_list(request,offset):
	if request.user.is_authenticated():
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		m = Article.objects.get(id=offset)
		m.delete()
	return HttpResponseRedirect("/")

def update(request,offset):
	if request.user.is_authenticated():
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		if request.method == 'GET':
			u = Article.objects.get(id=offset)
		#	u.title = request.GET["title"]
		#	u.content = request.GET["content"]
			image_urls   = Image.objects.get(pk=2)
			form = ArticleForm({'title':u.title,"content":u.content})
			return render_to_response("love_edit.html",{'name':request.user.username,'form':form,'image_urls':image_urls},context_instance=RequestContext(request))

		if request.method == "POST":
			u = Article.objects.get(id = offset)
			u.title = request.POST['title']
			u.content = request.POST['content']
			u.save()
			return HttpResponseRedirect("/")


########################################################
#def upload(request):
   # profile = request.user.get_profile()
#	if request.method == 'POST':
#		u = Upload.objects.all()
#		u.user  = request.user.username
	#	u.save()
#		form = UploadForm(request.POST, request.FILES)
#		if form.is_valid():
#			form.save()
#		return HttpResponseRedirect("/upload/")
#	return render_to_response("upload.html",{"name":request.user.username},context_instance=RequestContext(request))
#def upload(request):
###########################################################

def upload(request):
	if request.user.is_authenticated():
        	users = User.objects.filter(pk=request.user.id)
		image_urls   = Image.objects.get(pk=2)
		for user in users:
			if request.method == "POST":
            			form = UploadForm(request.POST, request.FILES,instance=user)			
			#print form
				if form.is_valid():
					m = Upload.objects.all()
					m = Upload(image=request.FILES['image'],user=request.user)
					m.save()
					data = form.save()
					data.save()
        			else:
            				form = UploadForm(instance=user)
				#return render_to_response('upload.html', { 'form' : form })
				return HttpResponseRedirect("/")

	return render_to_response("upload.html",{"user":user,"name":request.user.username,"image_urls":image_urls},context_instance=RequestContext(request))

def uploadchange(request):
	if request.user.is_authenticated():
		users = User.objects.filter(pk=request.user.id)
		image_urls = Image.objects.get(pk=2)
		uploadimages = Upload.objects.filter(user_id = request.user.id)
		#print image_urls.image

		for user in users:
			if request.method == "GET":
				u = Upload.objects.get(user_id = request.user.id)
				if u.user_id == None:
					#u.delete()
					print "u.user_id is None!!!"
			#	form = UploadForm(request.POST,request.FILFS,instance=user)
				
			#	if form.is_valid():
			#		m = Upload.objects.all()
			#		m = Upload(image=request.FILES['image'],user=request.user)
			#		m.save()
			#		data = form.save()
			#		data.save()
			#	else:
			#		form = UploadForm(instance=user)
					#return HttpResponseRedirect("/upload/")
				else:
					u.delete()
					return HttpResponseRedirect("/upload/")
	
	return render_to_response("uploadchange.html",{"user":user,"name":request.user.username,"image_urls":image_urls,"uploadimages":uploadimages},context_instance=RequestContext(request))
	

def usercenter(request,user):
	if request.user.is_authenticated():
		users = User.objects.all()
		user  = request.user.username
		image_urls  = Image.objects.get(pk=2)
		user_id = request.user.id
	return render_to_response("usercenter.html",{"users":users,"user":user,"image_urls":image_urls,"user_id":user_id,"name":request.user.username},context_instance=RequestContext(request))
		
def users(request):
	if request.user.is_authenticated():
		users = User.objects.all()
		user  = request.user.username
		for user_s in users:
                	image_urls   = Image.objects.get(pk=2)
			uploadimages = Upload.objects.filter(user_id = 1)

	return render_to_response("users.html",{"users":users,"user":user,"image_urls":image_urls,"uploadimages":uploadimages,"name":request.user.username},context_instance=RequestContext(request))

def about(request):
	if request.user.is_authenticated():
        	users = User.objects.all()
		image_urls  = Image.objects.get(pk=2)
	return render_to_response("about.html",{"users":users,"image_urls":image_urls,"name":request.user.username},context_instance=RequestContext(request))
		
def gonggao(request):
	messages = Gonggao.objects.all().order_by('-id')
	users = User.objects.all()
        user  = request.user.username
	image_urls  = Image.objects.get(pk=1)
	return render_to_response("inbox.html",{"messages":messages,"users":users,'user':user,'name':request.user.username,'image_urls':image_urls},context_instance=RequestContext(request))

def sendmessages_add(request):
	sendmessages = Sendmessage.objects.all()
	return render_to_response("node_sixin.html",{'name':request.user.username,'sendmessages':sendmessages},context_instance=RequestContext(request))

def sendmessages_save(request):
	
	if request.method == 'POST':
		sendmessages = Sendmessage(subject = request.POST['subject'],boby=request.POST['boby'],sender_id = request.user.id)
		sendmessages.save()
		return HttpResponseRedirect("/")	








'''def find_mimetype(filename):
    """In production, you don't need this,
    Static files should serve by web server, e.g. Nginx.
    """
    if filename.endswith(('.jpg', '.jpep')):
        return 'image/jpeg'
    if filename.endswith('.png'):
        return 'image/png'
    if filename.endswith('.gif'):
        return 'image/gif'
    return 'application/octet-stream'


def get_upload_images(request, filename):
    mimetype = find_mimetype(filename)
    with open(os.path.join(UPLOAD_AVATAR_UPLOAD_ROOT, filename), 'r') as f:
        return HttpResponse(f.read(), mimetype=mimetype)

def get_avatar(request, filename):
    mimetype = find_mimetype(filename)
    with open(os.path.join(UPLOAD_AVATAR_AVATAR_ROOT, filename), 'r') as f:
        return HttpResponse(f.read(), mimetype=mimetype)

@login_required
def home(request):
    try:
        u = User.objects.get(user_id=request.user.id)
    except User.DoesNotExist:
        html = '<html><body><a href="/upload">upload avatar</a></body></html>'
        return HttpResponse(html)

    imgs = map(lambda size: "<p><img src='%s'/></p>" % u.get_avatar_url(size), UPLOAD_AVATAR_RESIZE_SIZE)

    html = """<html>
    <body>
    <h2>%s <a href="/upload">upload avatar</a></h2>
    %s
    </boby>
    </html>""" % (request.user.username, '\n'.join(imgs))
    return HttpResponse(html)



@login_required
def upload(request):
    return render_to_response(
        'upload.html',
        get_uploadavatar_context(),
        context_instance = RequestContext(request)
    )
'''
	
