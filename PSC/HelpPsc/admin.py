from django.contrib import admin
from .models import Psc, Home ,Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Category,CategoryAdmin)    
# Register your models here.
class PscAdmin(admin.ModelAdmin):
    list_display = ('question','apple','boy','cat','dog','answer','category')

admin.site.register(Psc,PscAdmin)    


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title','description','link')

admin.site.register(Home,HomeAdmin) 