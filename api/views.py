from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model,authenticate
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,AllowAny


User= get_user_model()

class SignUpView(APIView):
    def post(self,request):
        serializers=Userserializer(data=request.data)
        if serializers.is_valid():
            user=serializers.save()
            if user.user_type == 'Client':
                send_mail(
                    'Verify your email',
                    'This is a Verification Mail',
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                )
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        
class UserLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'detail': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id':user.id,
                'user_type':user.user_type
            }, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        

class UploadFile(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.user_type == 'OpsUser':
            file = request.data.get('file')

            if not file:
                return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

            upload_file = FileUpload(file=file, uploaded_by=request.user)
            upload_file.save()

            return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


class DownloadFileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, file_id):
        try:
            file = FileUpload.objects.get(id=file_id)
        except FileUpload.DoesNotExist:
            return Response({'error':'File not Found'},status=status.HTTP_404_NOT_FOUND)
        
        if request.user.user_type != 'Client':
            return Response({'detail': 'Not authorized to download files.'}, status=status.HTTP_403_FORBIDDEN)
        

        download_link = request.build_absolute_uri(file.file.url)
        
        return Response({'download-link': download_link, 'message': 'success'})
    
class ListFiles(APIView):
    def get(self,request):
        if request.user.user_type != 'Client':
            return Response({'Not Authorized to Access'},status=status.HTTP_401_UNAUTHORIZED) 
        files=FileUpload.objects.all()

        download_links=[]

        for i in files:
            download_link = request.build_absolute_uri(i.file.url)
            download_links.append({'file':download_link})

        return Response(download_links)











        







