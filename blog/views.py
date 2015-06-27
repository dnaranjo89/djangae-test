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

    context_dict = {'articles': article_list, 'category': filter_category}
    return render(request, 'index.html', context_dict)


def new_article(request):
    """
    Add a new article to the DB
    """
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.validate():
            article = Article()
            form.populate_obj(article)
            article.put()

    context_dict = {'form': form}
    return render(request, 'new_article.html', context_dict)


def display_article(request, article_id):
    article = Article.get_by_id(int(article_id))
    article_form = ArticleForm(obj=article)
    context_dict = {'article_form': article_form}
    return render(request, 'display_article.html', context_dict)


def populate(request):
    """
    Populates the database with some Categories and Articles
    """
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