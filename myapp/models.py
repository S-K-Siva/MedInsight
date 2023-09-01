from django.db import models
from django.contrib.auth.models import User
# # Create your models here.
# class MyModel(models.Model):
#     creator = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="listings")

#     image_url = models.ImageField(null=True,blank=True,default="",upload_to="")
#     @property
#     def imageURL(self):
#         try:
#             url = self.image_url._url 
#         except:
#             url = ""
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class MyModel(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listings")
    # title = models.CharField(
    #     max_length=80, blank=False, null=False)
    # description = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)