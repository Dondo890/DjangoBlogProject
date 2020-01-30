from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here - Controller in Java.

#Controller for homepage
#Inject login required in page
@login_required
def HomePage(request):
    return render(request, 'html/home.html')


#ListView for list of post
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'html/home.html'
    context_object_name = 'posts'
    ordering = ['-date']

#DetailView for viewing individual post
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'html/postdetail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'html/postnew.html'
    fields = ['title', 'post']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'html/postnew.html'
    fields = ['title', 'post']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True;

        return False;

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'html/postdelete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True;
        return False;
