from django.shortcuts import render
from blog.models import *
from blog.forms import ArticleForm
from django.shortcuts import redirect

def index(request):
    filter_category = request.GET.get("category", "All")
    if filter_category and filter_category != "All":
        category_key = Category.all().filter('name =', filter_category).get()
        article_list = Article.all().filter('category =', category_key)
    else:
        article_list = Article.all()

    form = ArticleForm()

    context_dict = {'articles': article_list, 'category': filter_category, 'form':form}
    return render(request, 'index.html', context_dict)


# ===========  POPULATE  ==============
def populate(request):
    cat1 = add_category('Awesome stuff')

    add_article(category=cat1,
        title="Article1")

    add_article(category=cat1,
        title="Article2")

    add_article(category=cat1,
        title="Article3")

    cat2 = add_category("Colourful stuff")

    add_article(category=cat2,
        title="Article4")

    add_article(category=cat2,
        title="Article5")

    add_article(category=cat2,
        title="Article6")

    cat3 = add_category("Plain stuff")

    add_article(category=cat3,
        title="Article7")

    add_article(category=cat3,
        title="Article8")

    # Print out what we have added to the user.
    for c in Category.all():
        for a in Article.all().filter('category=',c):
            print "- Added {0} ({1})".format(str(a), str(c))

    return redirect('index')

def add_article(category, title, views=0):
    a = Article(category=category, title=title).put()
    a.views=views

    return a

def add_category(name):
    c = Category(name=name).put()
    return c