"""new_mustlovedoggo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
class Home(TemplateView):
     template_name = "index.html"
from django.views.generic import FormView
from django import forms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view()),
]


class NameForm(forms.Form):
          your_name = forms.CharField(label='Your name', max_length=100)
          first_name = forms.CharField(label='Your name', max_length=100)
          last_name = forms.CharField(label='Your name', max_length=100)

class FormClass(FormView):
        template_name = "index.html"
        form_class = NameForm

        def post(self, request, *args, **kwargs):
          """
          Handle POST requests: instantiate a form instance with the passed
          POST variables and then check if it's valid.
          """
          form = self.get_form()
          print(form)
          if form.is_valid():
              return self.form_valid(form)
          else:
              return self.form_invalid(form)
