from django.db import IntegrityError
rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'followed', 'followed_name'
            ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'you already follow this person'
            })