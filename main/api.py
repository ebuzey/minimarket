from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Product
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


@require_POST
@csrf_exempt
def cart_add_product(request):
    product_id = request.POST.get('product_id', None)
    if not product_id:
        return HttpResponseBadRequest('Invalid request, product_id required')
    session = request.session
    if 'cart' not in session.keys():
        session['cart'] = {}
    cart = session['cart']
    if product_id not in cart.keys():
        cart[product_id] = 1
    else:
        cart[product_id] += 1
    return JsonResponse(cart)