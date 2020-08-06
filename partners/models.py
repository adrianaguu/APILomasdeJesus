from django.db import models

class Opinion(models.Model):
	partner_name = models.CharField(max_length=100, unique=True)
	text = models.TextField(verbose_name="Texto de la Opinión")
	partner_photo = models.ImageField(verbose_name="Foto de Socio",upload_to='images/opinions/')

	def __str__(self):
		return self.partner_name

	class Meta:
		verbose_name = "Opinión"
		verbose_name_plural = "Opiniones"