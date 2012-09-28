from django.shortcuts import render_to_response
from django.template import RequestContext
from post.models import Post


def home(request):
    if request.POST:
        message = request.POST.get('post', '')
        if message:
            m = Post.objects.create(message=message)
    return render_to_response('home.html',
            {'posts': Post.objects.all().order_by('-id')},
            context_instance=RequestContext(request))
