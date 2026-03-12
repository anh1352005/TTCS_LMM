from django.shortcuts import render
from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Loan,LoanDetail
from .serializers import LoanDetailSerializer,LoanSerializer
# Create your views here.
class LoanView(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer

    @action(detail=True,methods=['patch'])
    def approve(self,request,pk=None):
        loan=self.get_object()
        
        for detail in loan.loan_details.all():
            book=detail.book
            if book.available_quantity<=0:
                return Response({
                    "error":f"{book.title} is not available"
                })
            book.available_quantity-=1
            book.save()
        loan.status="borrowed"
        loan.save()
        return Response({"message":"Loan Approved"})
    @action(detail=True,methods=['patch'])
    def return_book(self,request,pk=None):
        loan=self.get_object()
        
        for detail in loan.loan_details.all():
            book=detail.book
            book.available_quantity+=1
            book.save()

        loan.status="returned"
        loan.return_date=date.today()
        loan.save()

        return Response({"message":"Book Returned"})

    @action(detail=False,methods=['get'])
    def my_loans(self,request):
        loans=Loan.objects.filter(user=request.user)
        serializer=self.get_serializer(loans,many=True)
        return Response(serializer.data)

class LoanDetailView(viewsets.ModelViewSet):
    queryset=LoanDetail.objects.all()
    serializer_class=LoanDetailSerializer

