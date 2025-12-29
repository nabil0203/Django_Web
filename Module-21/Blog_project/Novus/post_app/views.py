from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Tag, Comment, Post

from django.db.models import Q                          # used in 'search'

from django.core.paginator import Paginator

from django.contrib.auth.models import User

from . import forms                                                 # live-2

from django.contrib.auth.forms import UserCreationForm                # live-2

from django.contrib.auth import login                                 # live-2

from django.contrib.auth.decorators import login_required                # live-2




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
            Q(title__icontains = searchQ) |                                                     # icontains = converts all the searched text into lower case [no sensitive]
            Q(content__icontains = searchQ)   |
            Q(category__name__icontains = searchQ)  |
            Q(tag__name__icontains = searchQ)
        ).distinct()                                                                            # if search = "Python"; then post will show once for title, once for content, once for tag
                                                                                                # 'distinct' used to show the search result once
                                                                                               

                                                                        

    paginator = Paginator(posts, 2)                                                             # 2 posts per page: 100 post = 50 page
    page_number = request.GET.get('page')                                                       # '?page=8' {user query}
    page_obj = paginator.get_page(page_number)                                                  # if page exists, it will show the posts of that page



    context = {                                                                                 # things that will go to the frontend
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'search_query': searchQ,
        'category_query': categoryQ,
        'tag_query': tagQ,
    }



    return render(request, 'blog/post_list.html', context)






# ------------------------ Live - 2 ---------------------------------------


# create post
# import the form
@login_required
def post_create(request):

    if request.method == 'POST':
        form = forms.PostForm(request.POST)                     # the data submitted by the user submitted in the form, we will get those data by the `post request`
        if form.is_valid():
            form = form.save(commit=False)                     # commit=false bcz we have some fields of Post Model remaining
            form.author = request.user
            form.save()

            return redirect('post_list')
        

    else:                                                # else means GET request
        form = forms.PostForm()

    return render(request, 'blog/post_create.html   ',{'form' : form})






# update post
# import get_object_or_404
@login_required
def post_update(request, id):                                               # 'id' needed bcz just 1 specific id update at a time

    post = get_object_or_404(Post, id=id)                                   # matching the 'id' of the post, with the 'id' I want to edit; if it's matched then stored in 'post'
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance=post)               # instance = post; if user goes for update menu but does't update/change anything and save it, then this handles it
                                                                         # request.POST; if user goes for update menu and updates/changes anything
        if form.is_valid():
            form.save()
            return redirect('post_list')
        

    else:                                                       # else means GET request
        form = forms.PostForm(instance=post)                    # instance=post means user will see the object always filled up with the data

    return render(request, 'blog/post_create.html',{'form' : form})








# delete post
@login_required
def post_delete(request, id):                                    # 'id' needed bcz just 1 specific id delete at a time
    
    post = get_object_or_404(Post, id=id)
    post.delete()

    return redirect('post_list')







# read post
@login_required
def post_details(request, id):

    post = get_object_or_404(Post, id=id)

    # comment form handle
    # take comment in a form                                    [same as 'create post' form -->post_create]
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_details', id=post.id)               # id=post.id means, it will show the same post that I am commenting on

    else:
        form = forms.CommentForm()




    # show comments [for specific posts]
    comments = post.comment_set.all()                                             # Comment and Post == 1 to Many; all comments of a post will be shown



    # post is already Liked by the user or not
    is_liked = post.liked_users.filter(id=request.user.id).exists()                         # filtering 'liked_user' of the model; "id = request.user.id" -> matching the 'liked_user' ID with the ID of the currently logged-in user.



    # like count
    like_count = post.liked_users.count()




    context = {
        'post' : post,
        'categories' : Category.objects.all(),
        'tag' : Tag.objects.all(),
        'comments' : comments,
        'is_liked' : is_liked,
        'like_count' : like_count,
        'comment_form' : forms.CommentForm
    }



    # post view count[impression]
    post.views_count += 1                                                   # 'views_count' in DB; default = 0; increments every time the post is seen
    post.save()



    return render(request, 'blog/post_details.html', context)












# Like post
@login_required
def like_post(request, id):

    post = get_object_or_404(Post, id=id)                                       # like 1 specific post


    if post.liked_users.filter(id = request.user.id):                                # user already liked the post
        post.liked_users.remove(request.user)                                        # can't like again, like will be removed


    else:                                                           #  user did not liked the post
        post.liked_users.add(request.user)                           # therefore add the user into liked_user list


    return redirect('post_details', id=post.id)                      # id=post.id means, it will show the same post that I am Liking









# sign up user
# same as 'post_create'
# import 'UserCreationForm'
def signup_view(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('post_list')
        

    else:                                                # else means GET request
        form = UserCreationForm()


    return render(request, 'user/signup.html', {'form' : form})







# user profile page
# Profile page
@login_required
def profile_view(request):
    section = request.GET.get('section', 'profile')
    context = {'section' : section}
    
    if section == 'posts':
        posts = Post.objects.filter(author = request.user)
        context['posts'] = posts 
    
    elif section == 'update':
        
        if request.method == 'POST':
            form = forms.UpdateProfileForm(request.POST, instance=request.user)                 # 'instance=request.user' = specific user's content will be shown to update
            if form.is_valid():
                form.save()
                return redirect('/profile?section=update')
                
        else:
            form = forms.UpdateProfileForm(instance=request.user)
    
        context['form'] = form
    
    return render(request, 'user/profile.html', context)