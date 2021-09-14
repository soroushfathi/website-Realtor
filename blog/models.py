from django.db import models

class SingleBlog(models.Model):
    title        = models.CharField(max_length=80, blank=False)
    introduction = models.CharField(max_length=300, blank=True)
    body         = models.TextField(blank=False)
    main_photo   = models.ImageField(blank=True)

