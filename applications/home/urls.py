from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('add-subscription',views.SubcriberCreateView.as_view(), name='add_subscription'),
    path('message-contact',views.ContactCreateView.as_view(), name='message_contact')
]
