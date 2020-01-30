from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import Detail, Comment
from datetime import datetime
def index(request):
    items = Detail.objects.order_by('-price')
    context = {
        'items': items
    }
    return render(request, 'index.html', context)

def details(request, details_id):

    if request.method == 'POST':
        user_id = request.POST['user_id']
        massage = request.POST['massage']
        post_id = details_id
        query = Comment(massage=massage)
        query.user_id_id = user_id
        query.post_id_id = post_id
        query.save()
    item = get_object_or_404(Detail, pk=details_id)
    comment = Comment.objects.all().filter(post_id=details_id)
    context = {
        'item': item,
        'comments': comment,
    }
    return render(request, 'details.html', context)