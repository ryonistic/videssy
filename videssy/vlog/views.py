from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from .models import Video, Comment
from .forms import CreateVideoForm, CreateCommentForm


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

class CreateVideoView(SuccessMessageMixin, CreateView):
    template_name = 'create_video.html'
    form_class = CreateVideoForm
    success_message = 'Video Uploaded.'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        video = form.save(commit=False)
        video.uploader = self.request.user 
        self.object = video.save()
        messages.success(self.request, 'Video Uploaded successfully.')
        return redirect('home')

