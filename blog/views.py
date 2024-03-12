from .models import statia
from .models import document
from .forms import docform
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required

def upload_document(request):
    if request.method == 'POST':
        form = docform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')   # перенаправить на страницу "успешной загрузки"
    else:
        form = docform()
    return render(request, 'blog/upload_document.html', {'form': form})

def success(request):
    return render(request, 'blog/success.html')
def document_list(request):
    documents = document.objects.all()
    return render(request, 'blog/document_list.html', {'documents': documents})

class shownews(ListView):
    model=statia
    template_name='blog/home.html'
    context_object_name='news'
    ordering=['time']
    def get_context_data(self,**kwargs):
        ctx=super(shownews,self).get_context_data(**kwargs)
        ctx['title']='Басты бет'
        return ctx

class NewsDetail(DetailView):
  
    model=statia
    template_name='blog/news_detail.html'
    def get_context_data(self,**kwards):
        ctx=super(NewsDetail,self).get_context_data(**kwards)
        ctx['title']=statia.objects.get(pk=self.kwargs['pk'])
        return ctx

class creatnew(LoginRequiredMixin,CreateView):
   
    model=statia
    template_name='blog/create_news.html'
    fields=['title','poto','text']
    def get_context_data(self,**kwards):
        ctx=super(creatnew,self).get_context_data(**kwards)
        ctx['title']='добавление статьи'
        ctx['btn_text']='добавить статьи'
        return ctx
    def form_valid(self,form):
        form.instance.adam=self.request.user
        return super().form_valid(form)
class updatview(LoginRequiredMixin,UpdateView):
   
    model=statia
    template_name='blog/create_news.html'
    fields=['title','poto','text']
    def get_context_data(self,**kwards):
        ctx=super(updatview,self).get_context_data(**kwards)
        ctx['title']='обнавление статьи'
        ctx['btn_text']='обнавить статьи'
        return ctx
    def form_valid(self,form):
        form.instance.adam=self.request.user
        return super().form_valid(form)
    
      
def pronas(request):
    f={'title':'Pro nas!'}
    return render(request,'blog/pronas.html',f)