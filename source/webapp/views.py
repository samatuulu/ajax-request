from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm


def contact_page(request):
    form = ContactForm
    return render(request, 'webapp/core/contact.html', {'contactForm': form})


def post_contact(request):
    if request.method == 'POST' and request.is_ajax():
        form = ContactForm(request.POST)
        form.save()
        return JsonResponse({"success": True}, status=200)
    return JsonResponse({"success":False}, status=400)
