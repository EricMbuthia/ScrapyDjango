from django.urls import path
from companies_data_str.views import CompanyList

urlpatterns = [
    path('', CompanyList.as_view(), name = "company-list"),
]