from django.shortcuts import render
from rest_framework import viewsets
from users.models import Profile
from .models import Post
from .permissions import CustomReadOnly
from .serializers import PostSerializer, PostCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend
# view마다 필터 설정할 때 사용(settings.py에 이미 등록해서 상관없음)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [CustomReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['author', 'likes']


    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return PostSerializer
        return PostCreateSerializer


    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)

