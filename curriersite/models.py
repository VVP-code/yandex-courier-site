from django.db import models

# Create your models here.
from django.db import models

class Visitor(models.Model):
    user_id = models.CharField(max_length=36)  # uuid
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    visit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} — {self.ip_address} — {self.visit_date}"