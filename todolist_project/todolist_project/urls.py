from django.contrib import admin
from django.urls import path, include  # Ensure include is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  # Include the app's URLs
]