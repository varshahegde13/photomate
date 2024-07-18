from django.db import models

# Create your models here.
class Photographer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    portfolio_url = models.URLField()
    speciality = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    EVENT_TYPES = [
        ('W', 'Wedding'),
        ('B','Birthday'),
        ('C','Corporate'),
        ('O','Other'),
    ]
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    event_type = models.CharField(max_length=1,choices=EVENT_TYPES)
    Photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.client_name}- {self.event.title}'


    