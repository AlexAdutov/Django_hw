from django.db import models


class Phone(models.Model):

    # TODO: Добавьте требуемые поля
    name=models.CharField(max_length=50)
    price=models.FloatField()
    image=models.CharField(max_length=100)
    release_date=models.DateField()
    lte_exists=models.BooleanField()
    slug=models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = '-'.join(self.name.casefold().split(' '))
        super(Phone, self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.name}'
