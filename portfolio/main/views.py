from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Project, Tag


class ProjectList(ListView):
    template_name = "home.html"
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


def contact(request):
    return render(request, "contact.html")


class ShowProject(DetailView):
    template_name = 'project.html'
    model = Project