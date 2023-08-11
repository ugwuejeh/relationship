# # models.py

# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
#     # Add other fields as needed

#     def __str__(self):
#         return self.user.username

# class UserSettings(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     # Add other fields for user settings (e.g., theme, notification preferences, etc.)

#     def __str__(self):
#         return self.user_profile.user.username

    
# class Hobby(models.Model):
#     name = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.name
   
    
# class Person(models.Model):
#     name = models.CharField(max_length=50)
   

#     hobbies = models.ManyToManyField(Hobby, related_name='people')
   
    
#     def __str__(self):
#         return self.name

    

