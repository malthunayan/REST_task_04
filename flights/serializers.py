from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Flight, Booking

class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	first_name = serializers.CharField(required=True)
	last_name = serializers.CharField(required=True)
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name']

	def create(self, validated_data):
		user_obj = User(username=validated_data['username'], 
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'])
		user_obj.set_password(validated_data['password'])
		user_obj.save()
		return validated_data

class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

