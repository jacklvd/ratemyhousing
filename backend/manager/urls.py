from django.urls import path
from .views import CustomAuthToken, UserViewSet

urlpatterns = [
    path('create_account/', UserViewSet.as_view({'post':'create_account'})),    path('log_in/', CustomAuthToken.as_view()),
    path('log_out/', UserViewSet.as_view({'delete':'log_out'})),
    path('users/', UserViewSet.as_view({'get':'users'})),
]
