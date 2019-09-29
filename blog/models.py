from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def summary(self):
        return self.body[:100]
    
    def archive_date(self):
        return self.pub_date.strftime("%B %Y")
    
    def publish_date(self):
        return self.pub_date.strftime("%b. %d, %Y")

    def __str__(self):
        return self.title
    
    