from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment
from .forms import CleanUserRegisterForm  # Import your custom form if you created it

def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-date_posted')
    
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        if author and content:
            Comment.objects.create(
                post=post,
                author=author,
                content=content
            )
            return redirect('post-detail', pk=post.pk)
    
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post_detail.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def register(request):
    if request.method == 'POST':
        # Use your custom form if you created it, otherwise use UserCreationForm
        try:
            form = CleanUserRegisterForm(request.POST)
        except:
            form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # This will work now with redirect imported
    else:
        try:
            form = CleanUserRegisterForm()
        except:
            form = UserCreationForm()
    
    context = {
        'form': form,
        'title': 'Register'
    }
    return render(request, 'register.html', context)

# Optional: If you created the custom logout view
def custom_logout(request):
    from django.contrib.auth import logout
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('blog-home')
    return render(request, 'logout.html')