from django.shortcuts import render
from companies_data_str.models import CompanyItemModel
from django.views.generic import ListView
# Create your views here.

class BookList(ListView):
    model = CompanyItemModel
    template_name = "company_list.html"