
from django.urls import path

from apps.auth_token.views import AuthenticationModelForm

from apps.auth_token.api.logout import Logout

urlpatterns = [
    path('login/', AuthenticationModelForm.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
