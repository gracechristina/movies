from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    length = models.IntegerField()
    photo = models.ImageField(upload_to='list/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
class Theatre(models.Model):
    theatre_name = models.CharField(max_length=100, default="theatre")
    total_seats = models.IntegerField()

class Showtime(models.Model):
    show_date = models.DateTimeField(default=timezone.now)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre,on_delete=models.CASCADE)

class Comment(models.Model):
        post = models.ForeignKey("cinema.Post",on_delete=models.CASCADE, related_name="comments")
        author = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        approved_comment = models.BooleanField(default=False)

        def approve(self):
                self.approved_comment = True
                self.save()

        def __str__(self):
                return self.text

CATEGORIES = (  
    ('LAB', 'labor'),
    ('CAR', 'cars'),
    ('TRU', 'trucks'),
    ('WRI', 'writing'),
)
LOCATIONS = (  
    ('BRO', 'Bronx'),
    ('BRK', 'Brooklyn'),
    ('QNS', 'Queens'),
    ('MAN', 'Manhattan'),
    ('STN', 'Staten Island'),
)

class PostAd(models.Model):  
    name        = models.CharField(max_length=50)
    email       = models.EmailField()
    gist        = models.CharField(max_length=50)
    category    = models.CharField(max_length=3, choices=CATEGORIES)
    location    = models.CharField(max_length=3, choices=LOCATIONS)
    description = models.TextField(max_length=300)
    expire      = models.DateField()
