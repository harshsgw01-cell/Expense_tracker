from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, ExpenseSerializer
from .models import Expense


@api_view(["GET"])
def api_root(request):
    return Response({
        "message": "Django API is running",
        "endpoints": {
            "register": "/api/register/",
            "login": "/api/login/",
            "expenses": "/api/expenses/"
        }
    })


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)