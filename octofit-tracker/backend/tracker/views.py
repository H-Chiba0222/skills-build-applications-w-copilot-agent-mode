from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import User, Team, Activity
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        user = self.get_object()
        activities = Activity.objects.filter(user=user)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def leaderboard(self, request, pk=None):
        team = self.get_object()
        members = team.members.all()
        leaderboard = []
        for member in members:
            total_distance = Activity.objects.filter(user=member).aggregate(Sum('distance'))['distance__sum'] or 0
            leaderboard.append({
                'user': UserSerializer(member).data,
                'total_distance': total_distance
            })
        leaderboard.sort(key=lambda x: x['total_distance'], reverse=True)
        return Response(leaderboard)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
