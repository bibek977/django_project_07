from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

class ProfileView(APIView):
    def post(self,request,format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                'msg' : 'Resume uploaded',
                'status': 'success',
                'candiate': serializer.data },
            status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    def get(self, request, format=None):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return Response({
            'msg' : 'all candidates',
            'status' : 'success',
            'candidat' : serializer.data
        },
        status = status.HTTP_200_OK)