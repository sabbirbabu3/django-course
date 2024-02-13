from django.shortcuts import render, redirect
from .import forms
from .import models
from django.views.generic import CreateView, DeleteView,UpdateView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
def PostView(request):

    if request.method == 'POST':
        postFrom=forms.FromPost(request.POST)
        if postFrom.is_valid():
            # postFrom=postFrom.cleaned_data['author']=request.user
            postFrom.instance.author=request.user
            postFrom.save()
            return redirect("profile")
    else:
        postFrom=forms.FromPost()
    return render(request, 'post.html', {'form': postFrom})
#class base view
@method_decorator(login_required, name='dispatch')
class CreatPostView(CreateView):
    model=models.Post
    form_class=forms.FromPost
    template_name="post.html"
    success_url=reverse_lazy('profile')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    



def editView(request,id):
    post=models.Post.objects.get(pk=id)
    postFrom=forms.FromPost(instance=post)
    
    if request.method == 'POST':
        postFrom=forms.FromPost(request.POST,instance=post)
        if postFrom.is_valid():
            postFrom.save()
            return redirect('home')
    
    return render(request, 'post.html', {'form': postFrom})

#edit podt view using classbase view
@method_decorator(login_required, name='dispatch')
class EditpostView(UpdateView):
    model = models.Post
    form_class = forms.FromPost
    template_name = 'post.html'
    pk_url_kwarg = 'id'  # Correct attribute name
    success_url = reverse_lazy('profile')

def deleteView(request,id):
    data=models.Post.objects.get(pk=id)
    data.delete()
    return redirect('home_page')

# class base deleteView
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name='delete.html'
    success_url =reverse_lazy('profile')
    pk_url_kwarg= 'id'


class UserDetailView(DetailView):
    model = models.Post
    template_name= 'details.html'
    pk_url_kwarg= 'id'

    def post(self, request, *args, **kwargs):
        form=forms.CommentsPost(data=self.request.POST)
        post=self.get_object()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post  # Assign the current post to the comment
            new_comment.save()
            return self.get(request, *args, **kwargs)   

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object # post moder object akhane store korlm
        comments=post.comments.all()# post er vitore j related_name dewa seta ullek kora holo
       
        form=forms.CommentsPost()
        context['comments']=comments
        context['comments_form']=form
        return context



