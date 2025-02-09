from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=1)
    full_name = models.CharField(max_length=50)


class GameInformation(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    version = models.IntegerField()
    date_issue = models.DateField()
    company_name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
