from django.shortcuts import render

from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Profil, FriendRequest, Message
from .serializers import (UserSerializer, ProfileSerializer,
                           FriendRequestSerializer, MessageSerializer,)

from rest_framework.decorators import action
from rest_framework.response import Response




class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profil.objects.all()
    serializer_class = ProfileSerializer




class FriendRequestViewSet(viewsets.ModelViewSet):

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        friend_request = self.get_object()
        user1 = friend_request.from_user
        user2 = friend_request.to_user
        user1.profile.friends.add(user2.profile)
        user2.profile.friends.add(user1.profile)
        friend_request.delete()
        return Response({'status': 'friend request accepted'})





class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer



def home(request):
    return render(request, 'index.html')