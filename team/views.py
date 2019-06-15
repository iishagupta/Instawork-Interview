from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from .serializers import *
import json

# Create your views here.
class TeamView(APIView):
	def get(self, request):
		"""
		This API returns a single member or a list of members.
		If query param member_id is passed it will return single member object,
		or it will return a list of all members.

		Request URL: /team/[?member_id=<int>]
		Request Method: GET
		MemberObject: {firstName: str, lastName: str, email: str, mobile: str, role: str} 
		Response: {members: [MemberObject]} or {MemberObject}
		"""
		if 'member_id' in request.GET:
			return self.get_by_id(request.GET["member_id"])
		members = Member.objects.all() # select * from team_member
		membersArray = MemberSerializer(members, many=True).data
		return JsonResponse({
			'members': membersArray,
		})

	def get_by_id(self, member_id):
		"""
		Helper function which returns a single member object to the get function
		"""
		try:
			instance = Member.objects.get(pk=member_id)
		except Member.DoesNotExist:
			return JsonResponse({
				'error': f"Member ID {member_id} not found",
			}, status=404)
		return JsonResponse(MemberSerializer(instance).data)

	def post(self, request):
		"""
		This API creates a single member in the database.
		It will return the created member object as JSON in the 
		response.

		Request URL: /team/
		Request Method: POST
		Request Body: {firstName: str, lastName: str, email: str, mobile: str, role: str}
		Response: {firstName: str, lastName: str, email: str, mobile: str, role: str} 
		"""
		try:
			member = json.loads(request.body)
		except (ValueError, json.decoder.JSONDecodeError):
			return JsonResponse({
				'error': 'Malformed JSON'
			}, status=400)
		if 'id' in member:
			member.pop('id')
		serializer = MemberSerializer(data=member)
		try:
			serializer.is_valid(raise_exception=True)
		except ValidationError as e:
			return JsonResponse({
				'error': str(e)
			}, status=400)
		new_member = serializer.save()
		return JsonResponse(MemberSerializer(new_member).data)

	def put(self, request, member_id):
		"""
		This API is a partial/fully update on a MemberObject
		requires to specify member_id in the URL, and 
		"""
		try:
			data = json.loads(request.body)
		except (ValueError, json.decoder.JSONDecodeError):
			return JsonResponse({
				'error': 'Malformed JSON'
			}, status=400)
		try:
			instance = Member.objects.get(pk=member_id)
		except Member.DoesNotExist:
			return JsonResponse({
				'error': f"Member ID {member_id} not found"
			}, status=404)
		if 'id' in data:
			data.pop('id')
		serializer = MemberSerializer(instance=instance, data=data, partial=True)
		try:
			serializer.is_valid(raise_exception=True)
		except ValidationError as e:
			return JsonResponse({
				'error': str(e)
			}, status=400)
		updated_member = serializer.save()
		return JsonResponse(MemberSerializer(updated_member).data)

	def delete(self, request, member_id):
		try:
			instance = Member.objects.get(pk=member_id)
		except Member.DoesNotExist:
			return JsonResponse({
				'error': f"Member ID {member_id} not found"
			}, status=404)
		instance.delete()
		return JsonResponse({
				'message': f"Member ID {member_id} is deleted."
		})
