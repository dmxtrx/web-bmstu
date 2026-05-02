from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer


# Create your views here.

def home(request):
    return render(request, 'comments/home.html')

@api_view(['GET'])
def get_time(request):
    return Response({'time': timezone.now().isoformat()})

@api_view(['GET'])
def get_comments(request):
    comments = Comment.objects.order_by('-time')[:10]
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)