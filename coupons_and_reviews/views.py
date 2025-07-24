from rest_framework import viewsets, permissions
from common.permission import *
from .models import *
from .serializers import *

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAdminOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class AppliedCouponViewSet(viewsets.ModelViewSet):
    serializer_class = AppliedCouponSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        # Show only coupons used by the logged-in user
        if self.request.user.is_superuser:
            return AppliedCoupon.objects.all()
        else:
            return AppliedCoupon.objects.filter(customer=self.request.user)

