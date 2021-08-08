from django.urls import path

# from apps.boards.views import DetailBoardView
from apps.newsletter.views import NewsLetterModelForm, succes_new_subscriber, already_subscribe

app_name = 'newsletter'

urlpatterns = [
    path(
        'new/',
        NewsLetterModelForm.as_view(),
    ),
    path(
        'succes/',
        succes_new_subscriber,
         ),
    path(
        '<str:email>/',
        already_subscribe,
         ),
]