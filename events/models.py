from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')

class Achievement(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Weddings"
    count = models.PositiveIntegerField(default=0)  # Number to be displayed
    order = models.PositiveIntegerField(default=0)  # Order in the UI

    def __str__(self):
        return f"{self.name}: {self.count}"

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_starts_from = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    event_date = models.DateField()
    venue_location = models.CharField(max_length=255)
    additional_notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event_date}"

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} stars"