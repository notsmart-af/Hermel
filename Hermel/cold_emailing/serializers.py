# cold_emailing/serializers.py

from rest_framework import serializers
from cold_emailing.models import User, Campaign, Email, Contact, CampaignContact, EmailSettings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'
        
class EmailSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSettings
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CampaignContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignContact
        fields = '__all__'
        
        