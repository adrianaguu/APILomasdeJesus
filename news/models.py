from django.db import models
from django.utils import timezone

class Category (models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Categoría"

class News(models.Model):
	title  = models.CharField(verbose_name="Título",max_length=150, unique=True)
	texto = models.TextField(verbose_name="Texto")
	urlImage_wide = models.ImageField(verbose_name="Imagen Ancha",upload_to='images/news/wide/')
	urlImage_medium = models.ImageField(verbose_name="Imagen Mediana",upload_to='images/news/medium')
	urlImage_narrow = models.ImageField(verbose_name="Imagen Angosta",upload_to='images/news/narrow')
	category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="Categoría")
	views = models.IntegerField(verbose_name="Vistas",default=0)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Noticia"
