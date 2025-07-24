from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Login': reverse('api_login', request=request, format=format),
        'Categories': reverse('category-list', request=request, format=format),
        'Services': reverse('service-list', request=request, format=format),
        'Coupons': reverse('coupon-list', request=request, format=format),
        'Reviews': reverse('review-list', request=request, format=format),
        'Notifications': reverse('notification-list', request=request, format=format),
        'Galleries': reverse('gallery-list', request=request, format=format),
        'Appointments': reverse('appointment-list', request=request, format=format),
        'Stylist': reverse('stylist-list', request=request, format=format),
    })
