from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import redirect


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        try:
            request.user.auth_token.delete()
            return redirect('/')
        except User.auth_token.RelatedObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)