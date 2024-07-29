from django.shortcuts import render
from django.views.generic import TemplateView

class AccountPageView(TemplateView):
    template_name = "pages/accounts.html"
