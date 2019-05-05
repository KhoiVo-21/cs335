"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from polls import views as polls_views
from django.urls import include, path, re_path
from django.contrib import admin

admin.autodiscover()

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', polls_views.index),
    path('polls/<poll_id>/', polls_views.detail),
    path('polls/<poll_id>/results', polls_views.results),
    path('polls/<poll_id>/votes', polls_views.vote),
]
"""

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^polls/$', polls_views.index),
    re_path(r'^polls/(?P<poll_id>\d+)/$', polls_views.detail),
    re_path(r'^polls/(?P<poll_id>\d+)/results/$', polls_views.results),
    re_path(r'^polls/(?P<poll_id>\d+)/votes/$', polls_views.vote),
]