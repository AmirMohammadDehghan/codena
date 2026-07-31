from home import models
from blog.models import Post, Podcast


def search_context(request):
    try:
        global_search = models.Search.objects.all()
        global_course = models.Course.objects.all()
        global_post = Post.objects.all()
        global_podcast = Podcast.objects.all()
    except Exception as e:
        # مدیریت خطا (مثلاً لاگ کردن خطا)
        global_search = global_course = global_post = global_podcast = []

    return {
        'global_course': global_course,
        'global_post': global_post,
        'global_search': global_search,
        'global_podcast': global_podcast
    }
