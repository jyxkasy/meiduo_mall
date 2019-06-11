from django.conf.urls import url
from apps.users import views

urlpatterns = [
    url(r'^registration/$', views.RegisterView.as_view())
]