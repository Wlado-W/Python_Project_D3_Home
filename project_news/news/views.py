from django.views.generic import ListView
from django.views.generic import DetailView
from .models import News
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewsForm

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'

    def news_list(request):
        news = News.objects.order_by('-created_at')
        return render(request, 'news_list.html', {'news': news})

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

    def news_detail(request, pk):
        news = get_object_or_404(News, pk=pk)
        return render(request, 'news_detail.html', {'news': news})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})
