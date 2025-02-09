from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=1, verbose_name="сокращенное название")
    full_name = models.CharField(max_length=50, verbose_name="полное название")

    def __str__(self):
        return f"{self.name} - {self.full_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class GameInformation(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    version = models.IntegerField()
    date_issue = models.DateField()
    company_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name
