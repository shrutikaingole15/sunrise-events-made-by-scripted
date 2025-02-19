from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Booking, GalleryImage, Testimonial, Achievement
from django.contrib.auth.models import Group, User

admin.site.unregister(Group) 

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("name", "count", "order")
    list_editable = ("count", "order")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_starts_from', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'event_date', 'status')
    list_filter = ('status', 'service', 'event_date')
    search_fields = ('name', 'email', 'phone')
    date_hierarchy = 'event_date'
    actions = ['mark_as_confirmed', 'mark_as_rejected']

    def mark_as_confirmed(self, request, queryset):
        queryset.update(status='confirmed')
    mark_as_confirmed.short_description = "Mark selected bookings as confirmed"

    def mark_as_rejected(self, request, queryset):
        queryset.update(status='rejected')
    mark_as_rejected.short_description = "Mark selected bookings as rejected"

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'image_preview', 'created_at')
    list_filter = ('category', 'featured')
    search_fields = ('title', 'category')
    date_hierarchy = 'created_at'

    def image_preview(self, obj):
        return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.image.url)
    image_preview.short_description = 'Image Preview'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'is_active', 'created_at')
    list_filter = ('rating', 'is_active')
    search_fields = ('name', 'content')