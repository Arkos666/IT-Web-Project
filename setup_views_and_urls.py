def update_backend_views():
    views_content = """from django.shortcuts import render

def home(request):
    return render(request, 'backend/base.html')
"""
    with open('backend/views.py', 'w') as file:
        file.write(views_content)
    print("Updated backend/views.py")

def update_backend_urls():
    urls_content = """from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
"""
    with open('backend/urls.py', 'w') as file:
        file.write(urls_content)
    print("Updated backend/urls.py")

def update_project_urls():
    urls_content = """from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
]
"""
    with open('ITwebProject/urls.py', 'w') as file:
        file.write(urls_content)
    print("Updated ITwebProject/urls.py")

def main():
    print("Setting up views and URLs...")
    update_backend_views()
    update_backend_urls()
    update_project_urls()
    print("Setup completed.")

if __name__ == "__main__":
    main()
