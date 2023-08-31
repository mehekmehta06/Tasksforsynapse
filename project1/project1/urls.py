from django.contrib import admin
from django.urls import include
from django.urls import path
from primebinary import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('primebinary/', include('primebinary.urls')),
]
