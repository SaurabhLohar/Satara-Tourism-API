from django.db import models

# Create your models here.

class Place(models.Model):
	place = models.CharField(max_length=50)
	about = models.TextField(blank=False,null=False)
	location = models.CharField(max_length=50,null=False,blank=False)
	timing = models.CharField(max_length=50)
	entry_fee = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.place