from django.urls import path
from .views import cookie_standsList, cookie_standsDetail

urlpatterns = [
    path("", cookie_standsList.as_view(), name="thing_list"),
    path("<int:pk>/", cookie_standsDetail.as_view(), name="thing_detail"),
]
