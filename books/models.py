from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=255)
    note=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=255)
    published_year=models.IntegerField()
    publisher=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    
    category=models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books' #truy cập ngược tìm sách theo CAT
                             # category = Category.objects.get(name)
                             # category.books.all()
    )
    total_quantity=models.PositiveIntegerField(default=1)
    available_quantity=models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if self.available_quantity > self.total_quantity:
            self.available_quantity = self.total_quantity
        super().save(*args, **kwargs)