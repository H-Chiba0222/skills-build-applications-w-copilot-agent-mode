from rest_framework import serializers
from .models import User, Team, Activity
from bson import ObjectId

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture']

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members', 'created_at']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'description', 'duration', 'distance', 'calories', 'date', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convert ObjectId to string if needed
        if '_id' in representation:
            representation['id'] = str(ObjectId(representation['_id']))
        return representation