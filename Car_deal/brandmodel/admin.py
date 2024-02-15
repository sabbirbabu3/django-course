from django.contrib import admin
from .models import BarndModel  # Corrected the import statement

class BrandModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brand',)}  # Corrected the reference to 'brand'
    list_display = ['brand', 'slug']  # Displaying 'brand' and 'slug'

admin.site.register(BarndModel, BrandModelAdmin)  # Corrected the registration statement
