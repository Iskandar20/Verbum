from django.contrib.auth.models import User
from django.urls.base import reverse_lazy , reverse
from ggblog.models import Post
from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Category, Post , Comment
from .forms import EditForm, PostForm,CommentForm
from django.http import HttpResponseRedirect, request
  
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
         post.likes.remove(request.user)
         liked = False
    else:
       post.likes.add(request.user)
       liked = True

    return HttpResponseRedirect(reverse('BlogDeets', args=[str(pk)]))

class HomeView(ListView):
    model= Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data( *args, **kwargs)
        context["cat_menu"]= cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request, 'categories.html',{'cats':cats.title(),'category_posts' : category_posts})
    

class BlogDeetView(DetailView):
    model= Post
    template_name= 'blog_deets.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDeetView,self).get_context_data( *args, **kwargs)
        stuff = get_object_or_404(Post, id= self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id= self.request.user.id).exists():
            liked = True
        context["cat_menu"]= cat_menu
        context["total_likes"]= total_likes
        context["liked"]= liked
        return context    

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title','author','body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView,self).get_context_data( *args, **kwargs)
        context["cat_menu"]= cat_menu
        return context 
       
class AddCommentView(CreateView):
    model= Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'   

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView,self).get_context_data( *args, **kwargs)
        context["cat_menu"]= cat_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'
    #fields = ('title','title_tag','body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView,self).get_context_data( *args, **kwargs)
        context["cat_menu"]= cat_menu
        return context 

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'  
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView,self).get_context_data( *args, **kwargs)
        context["cat_menu"]= cat_menu
        return context   
