from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='api_login'),
]

# urlpatterns = [
#     path('api/', include((api_urlpatterns))),
# ]
