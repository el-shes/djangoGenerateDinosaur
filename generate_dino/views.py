from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import GeneratedDinoForm
from .models import Dino, GeneratedDino


# Create your views here.


class WelcomeView(TemplateView):
    template_name = 'generate_dino/welcome.html'


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'generate_dino/authorized.html'
    login_url = '/admin'


class DinoCreate(CreateView):
    model = GeneratedDino
    success_url = '/generated/dinos'
    form_class = GeneratedDinoForm


class DinosList(ListView):
    model = Dino
    context_object_name = "dinos"
    template_name = 'generate_dino/dinos_list.html'


class DinoDetailView(DetailView):
    model = Dino
    context_object_name = 'dino'
    template_name = 'generate_dino/detail_dino.html'


class GeneratedDinoList(ListView):
    model = GeneratedDino
    context_object_name = 'generated_dinos'


class DinosFilterList(ListView):
    model = Dino
    template_name = 'generate_dino/dinos_list.html'

    def get_queryset(self):
        query_set = self.model.objects.filter(name__istartswith='letter')
        return query_set
