from django.shortcuts import render
from django.contrib import messages
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
    paginate_by = 6

    def get_queryset(self):
        return Favorite.objects.favorite(self.request.user)


class FavoriteAddItems(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('users_app:userLogin')
    success_message = 'El post se agregó exitosamente'
    error_message ='Disculpa, algo salió mal. Probablemente el elemento ya está en favoritos o no existe.'
    template_name = 'favorites/list.html'

    def post(self, request, *args, **kwargs):
        try:
            user = self.request.user
            article = Article.objects.get(id=self.kwargs['pk'])
        
            query = Favorite.objects.create(
                user = user,
                article = article
            )
            messages.success(self.request, self.success_message)
        except:
            messages.error(self.request, self.error_message)    

        return HttpResponseRedirect(reverse('favorites_app:favoriteItems'))

class FavoriteRemoveDeleteView(generic.DeleteView):
    model = Favorite
    success_url = reverse_lazy('favorites_app:favoriteItems')
    success_message = 'El post se removió exitosamente'
    error_message ='Disculpa, algo salió mal. Probablemente el elemento no existe.'

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        if not object:
            messages.error(self.request, self.error_message)
        else:
            messages.success(self.request, self.success_message)
        
        return super(FavoriteRemoveDeleteView, self).delete(request, *args, **kwargs)  