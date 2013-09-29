#coding=utf-8

from django import forms
from django.forms import ModelForm
from cpython_forum.models import *

class NodeCateForm(forms.Form):
	name          = forms.CharField()
	description   = forms.CharField(widget=forms.Textarea )

class saysForm(forms.Form):
        content=forms.CharField(label="",widget=forms.Textarea)

class ArticleForm(forms.Form):
	title        = forms.CharField()
	content      = forms.CharField(widget=forms.Textarea )

class UploadForm(ModelForm):
	class Meta:
		model = Upload
		exclude = ("user")

class SendmessageForm(forms.Form):
	subject      =  forms.CharField()
	body         =  forms.CharField(widget=forms.Textarea)    
