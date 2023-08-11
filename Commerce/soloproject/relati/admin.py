from django.contrib import admin
from .models import UserProfile, UserSettings, Hobby, Person

@admin.register(UserProfile)
class Mymodel(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')
# Register your models here.
# admin.site.register(UserProfile)
admin.site.register(UserSettings)
admin.site.register(Hobby)
admin.site.register(Person)
# admin.site.register(Person)
