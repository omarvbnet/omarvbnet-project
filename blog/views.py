from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(req):
	return render(req, 'blog/allblogs.html', {'blogs':Blog.objects})

def detail(req, blog_id):

	detailblog = get_object_or_404(Blog, pk=blog_id)
	return render(req, 'blog/detail.html', {'blog':detailblog})