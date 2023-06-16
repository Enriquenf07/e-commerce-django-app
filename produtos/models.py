from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    imagem = models.ImageField(upload_to='images')
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.nome}'
    
    def get_absolute_url(self):
        return reverse("produto_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super().save(*args, **kwargs)