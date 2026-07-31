from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView

from jdatetime import date as jdate
from jdatetime import datetime as jdatetime


def jalalidate(date):
    gregorian_date = date
    jalali_date = jdate.fromgregorian(date=gregorian_date).strftime("%Y/%m/%d")
    return jalali_date


# Create your views here.
def start_page(request):
    posts = models.Post.objects.all().order_by('-date')
    slider = models.Blog_Slider.objects.all()

    top_all = models.Post.objects.filter(trending=True).order_by('-date')
    top_articles = models.Post.objects.filter(trending=True).order_by('-date')[:3]
    latest_article = models.Post.objects.filter(trending=False).latest('date')
    top_articles = list(top_articles)  # تبدیل به لیست تا بتوانیم مقاله‌ها را اضافه کنیم

    top_articles = sorted(top_articles, key=lambda x: x.date, reverse=True)

    for item in posts:
        item.date = jalalidate(item.date)

    for item in top_all:
        item.date = jalalidate(item.date)

    for article in top_articles:
        gregorian_date = article.date
        jalali_date = jdate.fromgregorian(date=gregorian_date)
        jalali_date_str = f" روز {jalali_date.day} ماه {jalali_date.strftime('%B')} سال {jalali_date.year}"
        article.date = jalali_date_str

    latest_article.date = jalalidate(latest_article.date)
    context = {
        'posts': posts,
        'slider': slider,
        'latest_article': latest_article,
        'top_articles': top_articles,
        'top_all': top_all,
    }
    return render(request, 'start_page.html', context=context)


def detail_page(request, slug, pk):
    post = models.Post.objects.get(slug=slug, pk=pk)

    tamplate_name = 'detail_page.html'

    context = {
        'post': post
    }
    return render(request, tamplate_name, context=context)


class PostListView(ListView):
    paginate_by = 12  # تعداد آیتم‌ها در هر صفحه
    model = models.Post
    template_name = 'blog/postlist.html'  # مسیر به فایل template
    context_object_name = 'posts'  # نام شیئی که به template فرستاده می‌شود


class PodcastListView(ListView):
    paginate_by = 4  # تعداد آیتم‌ها در هر صفحه
    model = models.Podcast
    template_name = 'podcast/podcastlist.html'  # مسیر به فایل template
    context_object_name = 'podcasts'  # نام شیئی که به template فرستاده می‌شود


class PodcastDetailView(DetailView):
    model = models.Podcast
    template_name = 'podcast/podcast_detail.html'
    context_object_name = 'podcast'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['least_podcasts'] = models.Podcast.objects.all().order_by('-date')[:4]
        context['podcast'] = models.Podcast.objects.get(slug=self.kwargs['slug'], pk=self.kwargs['pk'])
        return context
