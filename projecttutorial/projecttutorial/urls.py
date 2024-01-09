"""
URL configuration for projecttutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projecttutorial import views  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('about-us/', views.aboutus,name="aboutus"),
    path('home/', views.homepage, name="home"),
    path('userform/', views.userform, name="userform"),
    path('djangoform/', views.djangoform, name="djangoform"),
    path('simpleCalculator/', views.simpleCalculator, name="simpleCalculator"),
    path('marksheet/', views.marksheet, name="marksheet"),
    path('getdata/', views.getdata, name="getdata"),
    path('postdata/', views.postdata, name="postdata"),
    path('course/', views.course),
    path('dynamic-route1/<int:id>', views.dynamicroute1),
    path('dynamic-route2/<str:string>', views.dynamicroute2),
    path('dynamic-route3/<slug:data>', views.dynamicroute3),
    path('newsdetails/<int:news_id>', views.newsdetails),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URLS, document_root = settings.MEDIA_ROOTS)
