# Django
from django.db import models

# Image Resizing
from django.core.files import File
from PIL import Image
from io import BytesIO


class Category(models.Model):
    """ Table Category on db """
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ['name'] # Order by name, alphabetically.
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Simple way to get category's url
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(
        to=Category,
        related_name='products', # Variable for Category.product.all()
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(
        upload_to='uploads/', blank=True, null=True
    )
    thumbnail = models.ImageField(
        upload_to='uploads/', blank=True, null=True
    ) # It's gonna be generated after image
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] # Most recent first
    
    def __str__(self):
        return self.name

    def get_category_name(self):
        return self.category.name
        
    def get_absolute_url(self):
        """ Simple way to get the product's url """
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        """ Simple way to get the product's image, if there's one """
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        """ Simple way to get the thumbnail """
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        """ 
        Make thumbnail if `self.get_thumbnail` is called
        and there's no thumbnail already setted on the object
        """
        img = Image.open(image)
        img.convert('RGB') # certain everything is ok with the img
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
        