from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Comment, Post
from .models import Category

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

   
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class' : 'form-control'}),
            'author': forms.TextInput(attrs={'class' : 'form-control','value' : '','id' : 'elder','type' : 'hidden' }),
            #'author': forms.Select(attrs={'class' : 'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet': forms.Textarea(attrs={'class' : 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class' : 'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet': forms.Textarea(attrs={'class' : 'form-control'}),
        }        