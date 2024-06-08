def update_project_urls():
    file_path = "ITwebProject/urls.py"
    with open(file_path, "w") as file:
        file.write("from django.contrib import admin\n")
        file.write("from django.urls import path, include\n")
        file.write("from django.http import HttpResponseRedirect\n\n")
        file.write("urlpatterns = [\n")
        file.write("    path('admin/', admin.site.urls),\n")
        file.write("    path('', lambda r: HttpResponseRedirect('backend/')),  # Redirection to 'backend'\n")
        file.write("    path('backend/', include('backend.urls')),  # Include backend urls\n")
        file.write("]\n")

    print(f"Updated {file_path}")

def main():
    print("Updating project URLs...")
    update_project_urls()
    print("URLs updated successfully.")

if __name__ == "__main__":
    main()
