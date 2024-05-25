from .models import Category


def active_tab(request):
    return {'active_tab': request.resolver_match.url_name}

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}