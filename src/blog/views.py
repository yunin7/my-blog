from django.template import loader, Context
from django.http import HttpResponse
from django.core.context_processors import csrf
from blog.models import BlogPost, PostNews
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def archive(request):
  """
  if request.method == 'POST':
    form = 
    if form.is_valid():
      form.save()
      redirect()
  """
  users = User.objects.all()
  posts = BlogPost.objects.all()
  news = PostNews.objects.all()[:5]
  t = loader.get_template('archive.html')
  ctx = { 'posts': posts , 'news': news, 'users' : users}
  ctx.update(csrf(request))
  c = Context(ctx)
  return HttpResponse(t.render(c))
  
