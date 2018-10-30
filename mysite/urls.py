from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(r'polls/', include('polls.urls')),
    path(r'admin/', admin.site.urls),
]