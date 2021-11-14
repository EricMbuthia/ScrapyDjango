from django.db import models

# Create your models here.
class CompanyItemModel(models.Model):
    company_name_raw  = models.CharField(max_length= 300)
    company_name_clean = models.CharField(max_length= 300)
    company_loc_raw = models.CharField(max_length= 300)
    company_biz_phone = models.CharField(max_length= 300)
    company_biz_email = models.CharField(max_length= 300)
    company_street_name = models.CharField(max_length= 300)
    company_postal_code = models.CharField(max_length= 300)

