"""URL_Shortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from users import views as users_views
from shorten import views as shorten_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views as dashboard_views

urlpatterns = [

    path('', shorten_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', users_views.register, name='register'),
    path('api/lineplot/', dashboard_views.LinePlotAllURLS.as_view(), name='lineplot'),
    path('api/lineplot/<slug:shortcode>',
         dashboard_views.LinePlotURL.as_view(), name='lineploturl'),

    path('api/countryplot/', dashboard_views.CountriesAllURLS.as_view(),
         name='countryplot'),
    path('api/countryplot/<slug:shortcode>',
         dashboard_views.CountriesURL.as_view(), name='countryploturl'),


    path('api/osplot/', dashboard_views.OsAllURLS.as_view(),
         name='osplot'),
    path('api/osplot/<slug:shortcode>',
         dashboard_views.OsURL.as_view(), name='osploturl'),

    re_path(r'^api/refererplot/(?P<shortcode>[a-zA-Z0-9]{6})?$',
            dashboard_views.RefererURL.as_view(), name='refererplot'),

    path('api/shorturls/', shorten_views.ListShortURLs.as_view(),
         name='ListShortURLS'),
    path('<slug:shortcode>', shorten_views.short_url_redirect, name='short_code'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
