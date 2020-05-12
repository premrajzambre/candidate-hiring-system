from rest_framework import serializers
from .models import applicant

class InterviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = applicant
        fields = ('email', 'full_name', 'contact', 'degree', 'degree_score','type','aptitude_score','technical_score','personality_score','average_score')

class SalaryPredictSerializers(serializers.Serializer):
    level = serializers.IntegerField(default=0)
