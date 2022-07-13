from multiprocessing.dummy import current_process
from django.shortcuts import redirect, render, reverse
from .forms import PageForm
from .models import Page
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
# Create your views here.


class PostListView(ListView):
    model = Page
    template_name = 'diary/page_list.html'
    context_object_name = 'page'
    ordering = ['-dt_created']
    paginate_by = 6
    page_kwarg = 'page'


def page_detail(request, page_id):
    object_detail = Page.objects.get(id=page_id)
    return render(request, 'diary/page_detail.html', {'object_detail': object_detail})


class PostCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_create.html'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id': self.object.id})


class PostUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_create.html'
    pk_url_kwarg = 'page_id'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id': self.object.id})


class PostDeleteView(DeleteView):
    model = Page
    template_name = 'diary/page_confirm.html'
    pk_url_kwarg = 'page_id'
    context_object_name = 'object'

    def get_success_url(self):
        return reverse('page-list')
