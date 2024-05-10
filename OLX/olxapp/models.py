from django.db import models

class product(models.Model):
    product_name=models.CharField(max_length=40)
    price=models.IntegerField()
    year_reg = models.CharField(max_length=20)
    product_image=models.ImageField(upload_to='media',null=True,blank=True)
    posted_time=models.DateTimeField(auto_now_add=True)
    product_desc=models.TextField()

    def __str__(self):
        return self.product_name

# class user(models.Model):
#     name=models.CharField(max_length=30)
#     place=models.CharField(max_length=40)
#     phone=models.IntegerField(default=0)
#     def __str__(self):
#         return self.name
