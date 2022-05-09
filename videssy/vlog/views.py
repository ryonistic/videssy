from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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
        context['comments_num'] = len(Comment.objects.filter(video__slug=self.kwargs['slug']))
        this_video = Video.objects.get(slug=self.kwargs['slug'])
        context['suggested_videos'] = Video.objects.filter(tag=this_video.tag)
        return context

class CreateVideoView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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

@login_required
def like_video(request, video_slug):
    if request.user.is_authenticated:
        video = Video.objects.get(slug=video_slug)
        if video in request.user.liked_videos.all():
            request.user.liked_videos.remove(*[video])
            video.likes -= 1
            video.save()
        else:
            request.user.liked_videos.add(*[video])
            video.likes += 1
            video.save()
        return redirect('video_player', video_slug)
    else:
        messages.success(request, 'You need to be logged in to do that.')
        return redirect('video_player', video_slug)

@login_required
def comments(request, video_slug):
    if request.user.is_authenticated and (request.method == "POST"):
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = Video.objects.get(slug=video_slug)
            comment.publisher = request.user
            comment.save()
            messages.success(request, 'Comment posted successfully')
            return redirect('comments', video_slug)
        else:
            messages.success(request, 'Error while making comment')
            return redirect('video_player', video_slug)
    else:
        form = CreateCommentForm
        comments = Comment.objects.filter(video__slug=video_slug).order_by('-published')
        return render(request, 'comments.html', {'form':form, 'comments':comments})

def search(request, search_str):
	videos = Video.objects.filter(title__contains=search_str)
	context = {'searched':search_str, 'videos':videos}
	return render(request, 'search_results.html', context)

