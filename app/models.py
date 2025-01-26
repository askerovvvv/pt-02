from django.db import models


# Create your models here.
class GameInformation(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    version = models.IntegerField()
    date_issue = models.DateField()
    company_name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
