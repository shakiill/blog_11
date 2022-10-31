from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView

from apps.blog.models import Blog, Category
from apps.front.forms import ContactForm
from apps.front.models import Contact


class HomeView(TemplateView):
    template_name = 'front/home.html'


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/contact/'
    template_name = 'front/contact.html'


class BlogListView(ListView):
    model = Blog
    template_name = 'front/all_blog.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['cat_list'] = Category.objects.all().order_by('name')
        return data


class PostView(TemplateView):
    template_name = 'front/post.html'
