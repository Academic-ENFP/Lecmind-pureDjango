"""patternProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from subject import views as subject_view

router = routers.DefaultRouter()
# router.register(r'subject', subject_view.SubjectViewSet, basename='subject')
router.register(r'lecture', subject_view.LectureViewSet, basename='lecture')
# router.register(r'notes', subject_view.NotesViewSet, basename='notes')
# router.register(r'analysis', analysis_view.AnalysisViewSet, basename='analysis')
# router.register(r'interaction', analysis_view.InteractionViewSet, basename='interaction')


urlpatterns = [
    # path(r'', TemplateView.as_view(template_name='index.html'),name='index'),
    # path(r'(learningPage)|(signin)|(timestamp)|(result)|(home)/', TemplateView.as_view(template_name='index.html'), name='route'),
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path(r'api-token-verify/', verify_jwt_token),
    path('', include('home.urls')),
    path('learning/', include('subject.urls')),
    path('analysis/', include('analysis.urls')),
    path('chrome/', include('chrome.urls')),
    path('google/', include('allauth.urls')),
]
