from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView
from .forms import MessageForm
from .models import Message


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


def message_text(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            msg = form.save()
            return redirect('preview', slug=msg.slug)
    else:
        form = MessageForm()
    return render(request, 'message.html',{'form':form})

def preview(request,slug):
    message = get_object_or_404(Message, slug=slug)
    return render (request, 'preview.html',{'message':message})
