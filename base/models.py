from django.db import models


# Create your models here.
class PersonalData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    phone_number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=500)
    qr_image = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'
