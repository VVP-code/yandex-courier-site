from django.shortcuts import render
from django.views.generic import TemplateView
import uuid
from .models import Visitor
# Create your views here.
class MainPage(TemplateView):
    template_name = 'curriersite/index.html'

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def get(self, request, *args, **kwargs):

        user_id = request.COOKIES.get('user_id')
        if not user_id:
            user_id = str(uuid.uuid4())


        city = request.COOKIES.get('city')
        name = request.COOKIES.get('name')


        ip_address = self.get_client_ip()


        Visitor.objects.create(
            user_id=user_id,
            ip_address=ip_address,
            city=city,
            name=name
        )


        response = super().get(request, *args, **kwargs)
        response.set_cookie('user_id', user_id, max_age=365*24*60*60)  # на год
        return response

class Benefits(TemplateView):
    template_name = 'curriersite/benefits.html'

class Requirements(TemplateView):
    template_name = 'curriersite/requirements.html'

class FAQ(TemplateView):
    template_name = 'curriersite/faq.html'