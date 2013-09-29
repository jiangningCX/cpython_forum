#coding=utf-8
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#import os
#from upload_avatar.signals import avatar_crop_done
#from upload_avatar.models import UploadAvatarMixIn
   

class Node(models.Model):
	name         = models.CharField(max_length=30)
        nodecate_id  = models.IntegerField()
	date         = models.DateTimeField(auto_now_add=True, blank=True)	

class NodeCategory(models.Model):
	name         = models.CharField(max_length=30)
	description  = models.TextField()
	parent       = models.CharField(default="/",max_length=30)

class Article(models.Model):
	title        = models.CharField(max_length=60)
	content      = models.TextField()		
	date         = models.DateTimeField(auto_now_add=True, blank=True)
	user         = models.CharField(max_length=120)
	username_id  = models.IntegerField()

class UserProfile(models.Model):
#	user        = models.CharField(max_lendth=120)
 	email       = models.CharField(max_length=120)
	description = models.TextField()
	website     = models.CharField(max_length=512)
	image       = models.ImageField('Label', upload_to='static/media/')
#	def __unicode__(self):
#		return self.user.username
class Gonggao(models.Model):
	title      = models.CharField(max_length=60)
	content      = models.TextField()
        date         = models.DateTimeField(auto_now_add=True, blank=True)

class Reply(models.Model):
	topic_id  = models.IntegerField()
	author    = models.ManyToManyField(UserProfile)
	content   =  models.TextField()
	date      =  models.DateTimeField(auto_now_add=True, blank=True)	

class Topic(models.Model):
	author      =  models.ManyToManyField(UserProfile)	
	title       =  models.CharField(max_length=512)
	content     =  models.TextField()
        replys      =  models.ManyToManyField(Reply) 
        nodeid      =  models.IntegerField()
	reply_count =  models.IntegerField()
	browse_count    = models.IntegerField()
	last_reply_date =  models.DateTimeField(auto_now_add=True, blank=True)	


class Notify(models.Model):
	topic_id  = models.IntegerField()
	author    = models.ManyToManyField(UserProfile)
	reply_id  = models.IntegerField()
	date      = models.DateTimeField(auto_now_add=True, blank=True)	
	
class says(models.Model):
	user = models.CharField(max_length=60)
        created = models.DateTimeField(auto_now_add=True)
        content = models.TextField()
        sayid   = models.IntegerField()

#class User(models.Model, UploadAvatarMixIn):
#    user = models.ForeignKey('auth.User', related_name='user_info')
#    avatar_name = models.CharField(max_length=128)

#    def get_uid(self):
#        return self.user.id

#    def get_avatar_name(self, size):
#        return UploadAvatarMixIn.build_avatar_name(self, self.avatar_name, size)


#def save_avatar_in_db(sender, uid, avatar_name, **kwargs):
#    if User.objects.filter(user_id=uid).exists():
#        User.objects.filter(user_id=uid).update(avatar_name=avatar_name)
#    else:
 #       User.objects.create(user_id=uid, avatar_name=avatar_name)

#avatar_crop_done.connect(save_avatar_in_db)

class Photo(models.Model):
	image = models.ImageField('Label',upload_to='path/')

class Celebrity(models.Model):
    name = models.CharField(max_length=30)

class Image(models.Model):
    celebrity = models.ForeignKey(Celebrity)
    image = models.ImageField('Label', upload_to='static/media/')

class InlineImage(admin.TabularInline):
    model = Image

class CelebrityAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Celebrity, CelebrityAdmin)

class Upload(models.Model):
        user        = models.OneToOneField(User,unique=True,related_name='profile')
        image       = models.ImageField('Label', upload_to='static/media/',null=True,blank=True)

class Sendmessage(models.Model):
	subject     = models.CharField(max_length=60)
	boby        = models.TextField()
	sender_id   = models.IntegerField()
