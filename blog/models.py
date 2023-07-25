from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey





class Category(MPTTModel):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    parent=TreeForeignKey('self', related_name="children", on_delete=models.SET_NULL,null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

class Tag(MPTTModel):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)


class Post(models.Model):
    author=models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='articles/')
    text=models.TextField()
    category=models.ForeignKey(Category, related_name='post',on_delete=models.SET_NULL, null=True)
    tag=models.ManyToManyField(Tag, related_name="post")
    create_at=models.DateTimeField(auto_now_add=True)

class Rece

# Create your models here.
