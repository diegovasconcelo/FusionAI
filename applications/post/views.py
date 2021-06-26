from django.shortcuts import render
from django.views import generic
from .models import Category, Article
from applications.favorites.models import Favorite

class ArticleList(generic.ListView):
    template_name = 'post/list.html'
    context_object_name = 'posts'
    paginate_by = 4

    
    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        
        return context

    def get_queryset(self):
        kw = self.request.GET.get('kword','')
        category = self.request.GET.get('category','')

        result = Article.objects.search_article(kw, category)

        return result


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'post/detail.html'
    
    def get_context_data(self, **kwargs):
        try:
            context = super(ArticleDetailView, self).get_context_data(**kwargs)
            user = self.request.user
            article = self.kwargs['slug']
            context['favorite'] = Favorite.objects.is_favorite(user, article)
        except:
            context['error'] = "Sorry, something went brong."
        
        return context





