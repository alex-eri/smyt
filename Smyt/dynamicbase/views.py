# Create your views here.
from django.core import serializers
from django.views.generic.edit import BaseFormView, ModelFormMixin, ProcessFormView, BaseUpdateView
from django.views.generic.list import BaseListView
import models
import forms
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.generic import ListView,DetailView, FormView, View, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Table(BaseListView):
    response_class = HttpResponse
    content_type = 'application/json'

    def get_queryset(self,**kwargs):
        table = self.kwargs.get('table') or self.request.GET.get('table') or None
        Model = getattr(models,table)
        if Model:
            return Model.objects.all()
        else:
            raise Http404

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        data = serializers.serialize('json', context['object_list'])
        return self.response_class(
            data,
            **response_kwargs
        )

    def post(self,**kwargs):
        print kwargs

class RowEdit(BaseUpdateView):
    response_class = HttpResponse
    content_type = 'application/json'

    def get_object(self, queryset=None):
        table = self.kwargs.get('table') or self.request.GET.get('table') or None
        Model = getattr(models,table)
        pk = self.kwargs.get('pk') or\
             self.request.GET.get('pk') or\
             self.request.POST.get('pk') or\
             None
        if pk:
            return Model.objects.get(pk=pk)
        return Model()

    def form_valid(self, form):
        form.save()
        return self.render_to_response({})
    def form_invalid(self, form):
        print form
        return HttpResponseBadRequest('Bad Values')

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        data = serializers.serialize('json', [self.object])
        return self.response_class(
            data,
            **response_kwargs
        )


class Home(TemplateView):
    template_name = 'dynamicbase/home.html'
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        table = self.kwargs.get('table') or self.request.GET.get('table') or None
        context['table'] = table
        context['tables'] = [(k,getattr(models,k)._meta,getattr(forms,k)()) for k in models.tables]
        return context
