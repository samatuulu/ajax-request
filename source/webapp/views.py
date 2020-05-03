from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .forms import ContactForm


class ContactAjax(View):
    form_class = ContactForm
    template_name = 'webapp/core/contact.html'

    def get(self, *args, **kwargs):
        form = self.form_class()
        return render(self.request,  self.template_name, {'contactForm': form})

    def post(self, *args, **kwargs):
        if self.request.method == 'POST' and self.request.is_ajax():
            form = self.form_class(self.request.POST)
            form.save()
            return JsonResponse({"success":True}, status=200)
        return JsonResponse({"success": False}, status=400)
