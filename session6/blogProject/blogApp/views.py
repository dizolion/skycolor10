from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def list(request):
    #Get every objects from Article
    articles = Article.objects.all()
    # return render(request, 'list.html', {'articles': articles})
    
    # articles_category = Article.objects.all().values_list('category').distinct()
    articles_category = Article.objects.all().values_list('category', flat=True).distinct()
    
    articles_hobby_num = Article.objects.filter(category='Hobby').count()
    articles_Food_num = Article.objects.filter(category='Food').count()
    articles_Programming_num = Article.objects.filter(category='Programming').count()

    articles.filter(category = 'Hobby')
    return render(request, 'list.html', {'articles': articles,
                                         'articles_category': articles_category,
                                         'articles_hobby_num': articles_hobby_num,
                                         'articles_food_num': articles_Food_num,
                                         'articles_programming_num': articles_Programming_num,
                                         })


def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('list')
    return render(request, 'new.html')

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render (request, 'detail.html', {'article': article}) 

def category(request, article_category):
    samecategory = Article.objects.filter(category=article_category)
    return render(request, 'category.html',
                  {'articles': samecategory,
                   'category': article_category})


