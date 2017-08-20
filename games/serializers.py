from rest_framework import serializers
from .models import Game
from rest_framework.validators import UniqueTogetherValidator

class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ('id', 'name', 'release_date', 'game_category')

		validators = [
	        UniqueTogetherValidator(
	            queryset=Game.objects.all(),
	            fields=('name')
	        )
	    ]


