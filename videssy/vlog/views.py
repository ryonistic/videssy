from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def vlog_video(request, video_id):
    return render(request, 'video_player.html', {'video_id':video_id})
