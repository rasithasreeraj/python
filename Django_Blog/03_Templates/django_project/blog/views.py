from django.shortcuts import render

posts = [
    {
    'author':'Rasitha Sreeraj',
    'title': 'Blog Post 1',
    'content': 'My first Post',
    'date_posted': 'Oct 9th 2018'
    },

    {
    'author':'Sreeraj AV',
    'title': 'My First Post',
    'content': 'First Post Content',
    'date_posted': 'Oct 3rd 2018'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title':'About'})



# Create your views here.
