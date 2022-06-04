import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from generation_service import create_new_dino_name
from .models import Dino, GeneratedDino

from string import ascii_lowercase


# Create your views here.


class WelcomeView(TemplateView):
    template_name = 'generate_dino/welcome.html'


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'generate_dino/authorized.html'
    login_url = '/admin'


class DinoCreateView(TemplateView):
    template_name = 'generate_dino/generateddino_form.html'

    def get_context_data(self, **kwargs):
        context = super(DinoCreateView, self).get_context_data(**kwargs)
        dino_name = self.kwargs.get('dino_name')
        if dino_name != 'empty':
            context['dino_name'] = dino_name
        else:
            context['dino_name'] = ''
        return context


class DinoCreate(View):
    def get(self, request, *args, **kwargs):
        name = create_new_dino_name()
        return HttpResponseRedirect(f'/generate/dinos/form/{name}')


class DinoSave(View):
    def get(self, request, *args, **kwargs):
        GeneratedDino(name=self.kwargs.get('dino_name')).save()
        return HttpResponseRedirect('/generate/dinos/all')


class DinosList(ListView):
    model = Dino
    context_object_name = "dinos"
    template_name = 'generate_dino/dinos_list.html'

    def get_context_data(self, **kwargs):
        context = super(DinosList, self).get_context_data(**kwargs)
        context['abc'] = ascii_lowercase
        return context


class DinoDetailView(DetailView):
    model = Dino
    context_object_name = 'dino'
    template_name = 'generate_dino/detail_dino.html'


class GeneratedDinoList(ListView):
    model = GeneratedDino
    context_object_name = 'generated_dinos'


class DinosFilterList(DinosList):

    def get_queryset(self):
        dinos = self.model.objects.filter(name__istartswith=self.kwargs.get('letter'))
        return dinos
