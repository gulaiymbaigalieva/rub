from django.db import models

# Create your models here.
class kafedra(models.Model):

    name = models.CharField(max_length=200, help_text=" ")

    def __str__(self):

        return self.name


from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Prepodavateli(models.Model):
    imya = models.CharField(max_length=200)
    login = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    kafedra = models.ManyToManyField(kafedra, help_text="  ")


    def __str__(self):

        return self.imya

    def get_absolute_url(self):

        return reverse('book-detail', args=[str(self.id)])