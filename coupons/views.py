from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm
from django.core.exceptions import ObjectDoesNotExist

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        print(1)
        code = form.cleaned_data['code']
        print(code)
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
        except ObjectDoesNotExist:
            print(3)
            request.session['coupon_id'] = None
    return redirect('cart_detail')