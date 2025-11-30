from django.shortcuts import render

from .models import Category, Tag, Comment, Post

from django.db.models import Q

from django.core.paginator import Paginator




# Post List
# Has Filtering option based on 'Category' and 'Tag'
# Has 'Search' option

def post_list(request):

    # filtering
    categoryQ = request.GET.get('category')                               # query [in urls it will show "category = ...... "]
    tagQ = request.GET.get('tag')                                         # query [in urls it will show "tag = ...... "]
    searchQ = request.GET.get('search')                                   # query [in urls it will show "search = ...... "]



    posts = Post.objects.all()                                    # fetched All posts



   # Filter posts by category
    if categoryQ:
        posts = posts.filter(category__name=categoryQ)                          # 'category' is the ForeignKey field in the Post model that links to the Category model
                                                                                # '__name' allows us to access the 'name' field of the related Category object
                                                                                # Example: if categoryQ = "Python", this returns all posts whose category name is "Python"

    # Filter posts by tags
    if tagQ:
        posts = posts.filter(tag__name=tagQ)




    # search
    # we search depending on title OR category OR tag OR content
    if searchQ:
        posts = posts.filter(                                                           
            Q(title__icontains = searchQ) |                                                     # icontains = converts all the searched text into case lower case [no sensitive]
            Q(content__icontains = searchQ)   |
            Q(category__name__icontains = searchQ)  |
            Q(tag__name__icontains = searchQ)
        ).distinct()                                                                            # 'distinct' used to show the search result once

                                                                        

    paginator = Paginator(posts, 2)                                                             # 2 posts per page
    page_number = request.GET.get('page')                                                       # 100 post = 50 page
    page_obj = paginator.get_page(page_number)                                                  # if page exists, it will show the posts of that page



    context = {                                                                                 # things that will go to the frontend
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'search_query': searchQ,
        'category_query': categoryQ,
        'tag_query': tagQ,
    }



    return render(request, '', context)



