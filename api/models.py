from django.db import models

# Create your models here.

GENDER = (
    ('male', 'male'),
    ('female', 'female'),
    ('others','others')
)

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(choices=GENDER, max_length=50)
    location = models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'static/images', blank=True)
    cv = models.FileField(upload_to='static/cv', blank=True)

    def __str__(self):
        return self.name