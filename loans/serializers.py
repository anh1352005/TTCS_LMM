from rest_framework import serializers
from .models import LoanDetail,Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        field='__all__'

class LoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoanDetail
        field='__all__'

