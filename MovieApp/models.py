from django.db import models

class AbstractModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Category(AbstractModel):
    view_count = models.IntegerField(default=0)

class SearchTag(AbstractModel):
    pass



# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def rating(self):
        return 0


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField(float)
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE,)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True)
    tags = models.ManyToManyField(SearchTag,blank = True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title




STAR_CHOICES = (
    (1,'*'),
    (2,'* *'),
    (3,'* * *'),
    (4,'* * * *'),
    (5,'* * * * *'),
)

class Review(models.Model):
    text = models.TextField(max_length=500)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    stars = models.IntegerField(choices= STAR_CHOICES, default = 1)
    review_is_active = models.BooleanField(default=True)
    review_created = models.DateTimeField(auto_now_add=True)
    review_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text