from django.shortcuts import render

def home_view(request):
    return render(request, 'backend/homepage.html')

def services_view(request):
    return render(request, 'backend/services_page.html')

def blog_view(request):
    return render(request, 'backend/blog_index_page.html')

def contact_view(request):
    return render(request, 'backend/contact_page.html')

def about_view(request):
    return render(request, 'backend/about_page.html')

def success_stories_view(request):
    return render(request, 'backend/success_stories.html')
