from rest_framework import serializers
from django.db import models
from adminaccounts.models import AdminAccount

class AdminAccountSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = AdminAccount
        fields = ['email', 'username', 'password', 'password2']
        

    def save(self):

        admin_account = AdminAccount(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'passwords must match'})
        
        admin_account.set_password(password)
        admin_account.save()
        return admin_account

class AdminLoginSerializer(serializers.ModelSerializer):

    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model= AdminAccount
        fields = ['email', 'username', 'password']

    def validate(self, data):
        pass