from django.shortcuts import render, get_object_or_404
from .models import Blog
from .Form import FeedBlogForm

def alist(request):
    model = Blog.objects.all()
    return render(request, 'list.html', {'model':model})

def feedblog(request):
    if request.method == 'POST':
        form = FeedBlogForm(request.POST)  # Correct usage of request.POST
        if form.is_valid():
            form.save()
            return render(request, 'form_end.html')  # Return a success page after form save
    else:
        form = FeedBlogForm()  # Create an empty form for GET requests

    return render(request, 'form.html', {'form': form})  # Return the form on GET or invalid POST

def detail_blog(request, pk):
    model = get_object_or_404(Blog,pk=pk)
    return render(request, 'detail.html', {'model':model})




