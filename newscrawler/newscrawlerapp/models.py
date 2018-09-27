from django.db import models

# Create your models here.
class NewsInfo(models.Model):
    headline = models.CharField(max_length=500)
    href = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    posting_date = models.CharField(max_length=255)
    full_news = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'headlines'
