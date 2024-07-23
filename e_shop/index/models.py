from django.db import models

# Create your models here.
# Чтобы оптимизировать код лучше писать номера в степени 2


class Category(models.Model):
    name = models.CharField(max_length=64)
    added_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    pr_name = models.CharField(max_length=256)
    pr_count = models.IntegerField()
    pr_des = models.TextField(blank=True)
    pr_price = models.FloatField()
    pr_photo = models.ImageField(upload_to='static/pr_img/')  # Куда будут падать фотки всех продуктов
    pr_category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.pr_name


class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()


    def __str__(self):
        return self.user_id
