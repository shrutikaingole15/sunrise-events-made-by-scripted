from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, GalleryImage, Testimonial, Booking, Achievement
from .forms import BookingForm, ContactForm

def home(request):
    services = Service.objects.filter(is_active=True)[:4]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    featured_images = GalleryImage.objects.filter(featured=True)[:6]
    achievements = Achievement.objects.all().order_by("order")

    context = {
        'services': services,
        'testimonials': testimonials,
        'featured_images': featured_images,
        'achievements' : achievements,
    }
    return render(request, 'events/home.html', context)

class ServiceListView(ListView):
    model = Service
    template_name = 'events/services.html'
    context_object_name = 'services'
    queryset = Service.objects.filter(is_active=True)

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'events/service_detail.html'


def gallery_view(request):
    images = GalleryImage.objects.all()  
    services = Service.objects.all()
    
    context = {
        'images': images,
        'services': services,
    }

    return render(request, 'events/gallery.html', context)

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'events/booking.html'
    success_url = '/booking'

    def form_valid(self, form):
        booking = form.save()
        messages.success(self.request, 'Your booking request has been submitted successfully!')
        
        # Send email notification
        subject = f"New Booking Request: {booking.name}"
        message = f"""
        A new booking request has been submitted:
        
        Name: {booking.name}
        Email: {booking.email}
        Phone: {booking.phone}
        Service: {booking.service}
        Event Date: {booking.event_date}
        Venue Location: {booking.venue_location}
        Additional Notes: {booking.additional_notes}
        """
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
        
        return super().form_valid(form)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Send email
            subject = f"New Contact Form Submission: {name}"
            email_message = f"""
            Name: {name}
            Email: {email}
            Phone: {phone}
            Message: {message}
            """
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('events:contact')
    else:
        form = ContactForm()
    
    return render(request, 'events/contact.html', {'form': form})