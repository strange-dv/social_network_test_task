from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from . import permissions


class PostView(ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsCreatorOrReadOnly]


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        post = models.Post.objects.get(id=pk)
        request.user.like(post)

        return Response({"status": "ok"})


class UnLikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        post = models.Post.objects.get(id=pk)
        request.user.unlike(post)
        return Response({"status": "ok"})
