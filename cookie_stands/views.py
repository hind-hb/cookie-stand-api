from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import cookie_stands
from .permissions import IsOwnerOrReadOnly
from .serializers import cookie_standsSerializer
from rest_framework.permissions import IsAuthenticated


class cookie_standsList(ListCreateAPIView):
    queryset = cookie_stands.objects.all()
    serializer_class = cookie_standsSerializer


class cookie_standsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated)
    queryset = cookie_stands.objects.all()
    serializer_class = cookie_standsSerializer
