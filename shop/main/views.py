from django.shortcuts import render
from django.views import View


class IndexView(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template, context={})


class DeliveryView(View):
    template = 'delivery.html'

    def get(self, request):
        return render(request, self.template, context={})


class ContactView(View):
    template = 'contact.html'

    def get(self, request):
        return render(request, self.template, context={})


class AboutView(View):
    template = 'about.html'

    def get(self, request):
        return render(request, self.template, context={})
