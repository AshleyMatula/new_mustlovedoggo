from django.views.generic import FormView
from django import forms

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
