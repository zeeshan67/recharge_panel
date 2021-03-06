"""recharge_panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from recharge_panel_app import views
from recharge_panel_app import AuthComplete
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login, name='view.login'),
    url(r'^login/$', views.login, name='view.login'),
    url(r'^logout/$', views.logout, name='view.logout'),
    url(r'^logout/login', views.login, name='view.login'),
    # url(r'^/login/registration',views.registration,name='view.registration'),
    url(r'^payments/', views.payments, name='view.payments'),
    url(r'^initiate_recharge/', views.initiate_recharge, name='view.initiate_recharge'),
    # url(r'^recharge_view_plan/', views.view_plan, name='view.view_plan'),
    # url(r'', include('social_auth.urls')),
    #   url(r'^$', TemplateView.as_view(template_name="login.html")),
]
