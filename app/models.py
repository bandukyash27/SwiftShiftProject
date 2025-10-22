from django.db import models

# Create your models here.


class ContactDetails(models.Model):
    name=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField(max_length=70)

    def __str__(self):
        return self.name
    


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title
    


class Booking(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    details = models.TextField(blank=True, null=True)
    booking_datetime = models.DateTimeField(blank=True, null=True)  # Changed name
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending'
    )

    def __str__(self):
        return f"{self.name} - {self.service.title} ({self.status})"
