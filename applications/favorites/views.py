from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .models import Favorite

from applications.post.models import Article


class FavoriteItemsListView(LoginRequiredMixin, generic.ListView):
    template_name = 'favorites/list.html'
    context_object_name = 'favorite_items'
    login_url = reverse_lazy('users_app:userLogin')

    def get_queryset(self):
        return Favorite.objects.favorite(self.request.user)


class FavoriteAddItems(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('users_app:userLogin')

    def post(self, request, *args, **kwargs):
        user = self.request.user
        article = Article.objects.get(id=self.kwargs['pk'])
        Favorite.objects.create(
            user = user,
            article = article
        )

        return HttpResponseRedirect(reverse('favorites_app:favoriteItems'))


class FavoriteRemoveDeleteView(generic.DeleteView):
    model = Favorite
    success_url = reverse_lazy('favorites_app:favoriteItems')

