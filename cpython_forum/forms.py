#coding=utf-8

from django import forms
from django.forms import ModelForm
from cpython_forum.models import *
from DjangoUeditor.widgets import UEditorWidget
from  DjangoUeditor.forms import UEditorField

class NodeCateForm(forms.Form):
	name          = forms.CharField()
	#description   = forms.CharField(widget=forms.Textarea )
	description   = UEditorField("描述",initial="abc",width=600,height=800)
	#description      = forms.CharField(label="内容",widget=UEditorWidget(width=800,height=500, imagePath='aa', filePath='bb',toolbars={}))
class saysForm(forms.Form):
#        content=forms.CharField(label="",widget=forms.Textarea)
	content      = forms.CharField(label="",widget=UEditorWidget(width=800,height=500, imagePath='aa', filePath='bb',toolbars={}))
	
class ArticleForm(forms.Form):
	title        = forms.CharField()
	#content      = forms.CharField(widget=forms.Textarea )
	content      = forms.CharField(label="",widget=UEditorWidget(width=800,height=500, imagePath='aa', filePath='bb',toolbars={}))

class UploadForm(ModelForm):
	class Meta:
		model = Upload
		exclude = ("user")
    
