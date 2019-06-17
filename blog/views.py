# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from blog.models import BlogPost, BlogPostForm

# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts,
        'form':BlogPostForm()}, RequestContext(request))

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp=datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')
