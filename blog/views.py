from django.shortcuts import render
from blog.models import *


def index(request):
    category_list = Category.objects.order_by('name')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'index.html', context_dict)


