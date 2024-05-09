"""main URL Configuration

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
from django.contrib import admin
from django.urls import path


from .views import home , PatientCreateView , PatientUpdateView,DocumentCreateView,PatientProfileView,DocumentUploadView, DisplayResponseView,SearchPageView,GeneratedReportView,TestResultUpdateView


urlpatterns = [
    path ('', home, name='home'),
    # path ('Tweet/', Tweet, name='Tweet'),
    path ('create/', PatientCreateView.as_view(), name='patient_create'),
    path ('update/<int:pk>', PatientUpdateView.as_view(), name='patient_update'),
    path ('document/', DocumentCreateView.as_view(), name='document_create'),
    path ('detail/<int:pk>', PatientProfileView.as_view(), name='patient_profile'),
    path ('upload/<int:pk>', DocumentUploadView.as_view(), name='document_upload'),
    path ('response/<int:patient_id>/<int:document_id>', DisplayResponseView.as_view(), name='response'),
    path ('search/', SearchPageView.as_view(), name='search'),
    path ('generatedreport/<int:pk>', GeneratedReportView.as_view(), name='generated_report'),
    path ('testresutupdate/<int:pk>', TestResultUpdateView.as_view(), name='testresut_update'),
]
