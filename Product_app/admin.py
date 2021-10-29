from django.contrib import admin

# Register your models here.
from .models import Category,Product,Images
admin.site.register(Category)
admin.site.register(Images)

# To add more images
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


#  to chage the view of profuct
class ProductAdmin(admin.ModelAdmin):
    list_display  = ['title','status','created_at','updated_at','image_tag']
    list_filter = ['title','created_at']
    list_per_page = 10
    search_fields = ['title','new_price','detail']
    #  to add more images 
    inlines = [ProductImageInline]
    
    
    
admin.site.register(Product,ProductAdmin)
