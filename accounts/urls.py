from django.conf.urls import url
from accounts.views import register

urlpatterns = [
    url(r'^register$', register, name="register")
    ]