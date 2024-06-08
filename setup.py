import os

# Nombres de proyecto y aplicación
project_name = "ITwebProject"
app_name = "backend"

# Directorios y archivos a crear
directories = [
    f"{app_name}/templates/{app_name}",
    f"{app_name}/static/{app_name}/css",
    f"{app_name}/static/{app_name}/js",
    f"{app_name}/static/{app_name}/images"
]

files = {
    f"{app_name}/models.py": "from django.db import models\n\n# Create your models here.",
    f"{app_name}/views.py": "from django.shortcuts import render\n\n# Create your views here.",
    f"{app_name}/urls.py": "from django.urls import path\n\nurlpatterns = []",
    f"{app_name}/templates/{app_name}/base.html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Home</title>\n</head>\n<body>\n    <h1>Welcome to ITwebProject</h1>\n</body>\n</html>",
    f"{app_name}/static/{app_name}/css/style.css": "/* Add your CSS here */",
    f"{app_name}/static/{app_name}/js/script.js": "// Add your JavaScript here"
}

def create_directories():
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def create_files():
    for file_path, file_content in files.items():
        with open(file_path, 'w') as file:
            file.write(file_content)
            print(f"Created file: {file_path}")

def main():
    print(f"Setting up the '{app_name}' app in the '{project_name}' project...")
    create_directories()
    create_files()
    print("Setup completed successfully.")

if __name__ == "__main__":
    main()
