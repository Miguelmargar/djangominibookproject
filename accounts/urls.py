from django.conf.urls import url
from accounts.views import register, profile, login

urlpatterns = [
    url(r'^login', login, name="login"),
    url(r'^register$', register, name="register"),
    url(r'^profile$', profile, name="profile"),
]