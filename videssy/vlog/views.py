from django.shortcuts import render
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from .models import Video


class HomeView(ListView):
    model = Video
    context_object_name = 'videos'
    template_name = 'home.html'


class VideoPlayerView(HitCountDetailView):
    model = Video
    template_name = 'video_player.html'
    context_object_name = 'video'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        'popular_videos': Video.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context
