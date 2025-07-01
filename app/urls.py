from django.contrib import admin
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # path("",views.indexviws, name='index'),
    path("",views.homepage),
    path("login",views.login),
    path('signIn',views.signIn),
    path('project',views.projectpage),
    path('exp',views.experince),
    path('biodata',views.biodata),
    path('fillBiodata',views.fillBiodata),
    path('fillexp',views.fillexp),
    path('fillproject',views.fillproject),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)