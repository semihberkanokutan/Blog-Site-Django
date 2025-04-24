from django.db import models
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Tag(models.Model):
    caption = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=50)
    image_name = models.ImageField()
    date = models.DateTimeField()
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

