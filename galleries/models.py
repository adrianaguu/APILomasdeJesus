from django.db import models

class Gallery (models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Galería"
		verbose_name_plural = "Galerías"

class ImageGallery(models.Model):
	name = models.CharField(max_length=100, unique=True, null=True)
	gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE,verbose_name="Galería")
	description = models.CharField(verbose_name="Descripción",max_length=300,blank=True,null=True)
	urlImage = models.ImageField(verbose_name="Imagen grade",upload_to='images/galleries/')
	urlImage_small = models.ImageField(verbose_name="Imagen pequeña",upload_to='images/galleries/',blank=True,null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Imagen"
		verbose_name_plural = "Imágenes"
