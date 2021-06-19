from rest_framework import serializers
from .models import AdminUser


class AdminUserSerializer(serializers.Serializer):
    class Meta:
        model = AdminUser
        fields = ('id', 'username', 'email', 'first_name')


# |Register serializers
class RegisterSerializer(serializers.Serializer):
        class Meta:
            model = AdminUser
            fields = ('id', 'username', 'email', 'first_name', 'password')
            extra_kwargs = {'password':{'write_only':True}}


        def create(self, validated_data):
            return AdminUser.objects.create(**validated_data)
        # def create(self, validated_data):
        #     user = AdminUser.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        #     return user
