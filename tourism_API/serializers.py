from rest_framework import serializers
from .models import Place



class PlacesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = [
		'id','place','about','location','timing','entry_fee']