from django.shortcuts import render, redirect, get_object_or_404
from urllib.parse import urlencode
from .models import QR_link
from .forms import CreateNewLink

BASE_URL = "wapplink.me"
API_WHATSAPP = "https://api.whatsapp.com"
# Create your views here.


def home_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, "home.html", {
            'form': CreateNewLink,
            'qr_url': False,
        })
    else:
        qr_link = QR_link.objects.create(
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        return render(request, 'home.html', {
            'form': CreateNewLink,
            'qr_url': BASE_URL + '/' + qr_link.key
        })


def contact_view(request, *args, **kwargs):
    return render(request, "contact-us.html", {})


def create_link(request, *args, **kwargs):
    # TODO: remove
    if request.method == 'GET':
        return render(request, "create-qr-form.html", {
            'form': CreateNewLink,
        })
    else:
        qr_link = QR_link.objects.create(
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        return render(request, 'qr-img.html', {
            'qr_url': BASE_URL + '/' + qr_link.key
        })


def create_redirect(request, *args, **kwargs):
    # import pdb; pdb.set_trace()
    if 'key' in kwargs and kwargs['key']:
        data = get_object_or_404(QR_link, key=kwargs['key'])
        params = {'phone': data.phone, 'text': data.message}
        url = API_WHATSAPP + '/send' + '?' + urlencode(params)
        redirect(url)
    else:
        return render(request, "test.html", {})
