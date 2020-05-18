from django.db import models

class Job(models.Model):
	image = models.ImageField(upload_to = 'images/')
	video = models.FileField(upload_to = 'images/')
	summary = models.CharField(max_length = 200)
	pub_date = models.DateTimeField()
	body = models.TextField()

