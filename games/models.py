from django.db import models

# Create your models here.
class Game(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, null=False)
	release_date = models.DateTimeField(null=False)
	game_category = models.CharField(max_length=200, null=False)
	played = models.BooleanField(null=False)

	class Meta:
		ordering = ('name',)
