from rest_framework import serializers
from .models import Member
from collections import OrderedDict

#Copied from https://stackoverflow.com/questions/28945327/django-rest-framework-with-choicefield
class RoleChoicesField(serializers.Field): 
    def __init__(self, choices, **kwargs):
        self._choices = OrderedDict(choices)
        super(RoleChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        for i in self._choices:
            if self._choices[i] == data:
                return i
        raise serializers.ValidationError(
        	"Acceptable values are {0}.".format(list(self._choices.values())))


class MemberSerializer(serializers.Serializer):
	"""
	This class will be used to serialize/deserialize MemberObject data.
	It also has create and update function which will be used by the POST and
	PUT request respectively.
	"""
	id = serializers.IntegerField(required=False)
	firstName = serializers.CharField(max_length=200)
	lastName = serializers.CharField(max_length=200)
	email = serializers.CharField(max_length=200)
	mobile = serializers.CharField(max_length=14) 
	role =  RoleChoicesField(Member.ROLE_CHOICES)


	def create(self, validated_data):
		return Member.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.firstName = validated_data.get('firstName', instance.firstName)
		instance.lastName = validated_data.get('lastName', instance.lastName)
		instance.email = validated_data.get('email', instance.email)
		instance.mobile = validated_data.get('mobile', instance.mobile)
		instance.role = validated_data.get('role', instance.role)
		instance.save()
		return instance

	



