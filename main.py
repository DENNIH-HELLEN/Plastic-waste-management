from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")


from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helloworld_app.urls')),
]
