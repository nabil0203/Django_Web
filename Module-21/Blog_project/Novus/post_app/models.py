from django.db import models

from django.contrib.auth.models import User                 # user model import

from ckeditor.fields import RichTextField                   # Rich text field





#Different Category
class Category(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    




#Different Tag
class Tag(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name





# Post
class Post(models.Model):

    title = models.CharField(max_length=255)
    content = RichTextField()                                                             # Rich Text field
    author = models.ForeignKey(User, on_delete=models.CASCADE)                            # Author of the post [User & Post -> 1 to Many]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)                      # Category of the post [Category & Post -> 1 to Many]
    # comment = models.ForeignKey(Comment)                                                  # Comment of the post [Comment & Post -> 1 to Many]
    tag = models.ManyToManyField(Tag)                                                     # Tag of the post [Comment & Post -> Many to Many]
    liked_users = models.ManyToManyField(User, related_name='liked_posts', blank=True)                  # who who liked in the post [ User & Like -> Many to Many]
    views_count = models.BigIntegerField(default = 0)                                     # how many people have seen the post [count increment in each reload]

    created_at = models.DateTimeField(auto_now_add=True)                                    # The Creation time of an Object will be stored Automatically 
    updated_at = models.DateTimeField(auto_now=True)                                        # The Updating time of an Object will be stored Automatically 


    def __str__(self):
        return self.title
    




# Comment
class Comment(models.Model):

    content = models.TextField()                                                        # considering the comment as content
    user = models.ForeignKey(User, on_delete=models.CASCADE)                            # comment of the post [1 to Many]
    post = models.ForeignKey(Post, on_delete=models.CASCADE)                            # 1 post can have multiple comments [1 to Many]
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    
