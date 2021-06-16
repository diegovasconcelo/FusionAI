from django.urls import path
from . import views

app_name = 'favorites_app'

urlpatterns = [
    path('favorites/', views.FavoriteItemsListView.as_view(), name='favoriteItems'),
    path('favorites-add/<pk>/', views.FavoriteAddItems.as_view(), name='favoriteAdd'),
    path('favorites-remove/<pk>/',views.FavoriteRemoveDeleteView.as_view(), name='favoriteRemove')
]