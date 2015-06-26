from django.shortcuts import render
from blog.models import *
from django.shortcuts import redirect

def index(request):
    article_list = Article.objects.order_by('title')[:10]
    context_dict = {'articles': article_list}
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

    cat2 = add_category("Colourfull stuff")

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
    for c in Category.objects.all():
        for a in Article.objects.filter(category=c):
            print "- Added {0} ({1})".format(str(a), str(c))

    return redirect('index')

def add_article(category, title, views=0):
    a = Article.objects.get_or_create(category=category, title=title)[0]
    a.views=views
    a.save()
    return a

def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c