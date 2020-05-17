from django.shortcuts import render, redirect

# Create your views here.
def blog(request):
	return render(request, 'career/blog.html', {})

def aboutc(request):
	return render(request, 'career/about_candidate.html', {})
