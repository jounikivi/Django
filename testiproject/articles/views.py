from django.shortcuts import render
from .models import Article

# Create your views here.

def Article_search(request):

    context ={}
    return render(request, 'articles/search.html', context=context)



def Artcile_Detail(request, id=None):
    article_obj = Article.objects.get(id=id)
    article_obj = None
    if id is not None:
        Article.objects.get(id=id)

    contex = {
        'object': None,
    }

    return render(request, 'articles/detail.html', context=contex)