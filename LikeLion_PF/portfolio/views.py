from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator

from .models import Portfolio
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import PortfolioForm
from django.core.paginator import Paginator

class PortfolioCreateView(CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio/upload.html'

    # 작성된 내용 검증
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})

class PortfolioDeleteView(DeleteView):
    model = Portfolio
    success_url = '/'
    template_name = 'portfolio/delete.html'

    def get(self, request, *args, **kwargs):
        object_instance = self.get_object()  # Get the object
        object_user = object_instance.author  # Get the user who owns the object

        user = get_object_or_404(User, username=self.request.user)  # Get the user in the view
        if object_user != user:  # See if the object_user is the same as the user
            return HttpResponseForbidden('Permission Error')
        else:
            return render(request, self.template_name, {'object': object_instance})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class PortfolioUpdateView(UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio/update.html'

    def get(self, request, *args, **kwargs):
        object_instance = self.get_object()  # Get the object
        object_user = object_instance.author  # Get the user who owns the object

        user = get_object_or_404(User, username=self.request.user)  # Get the user in the view
        if object_user != user:  # See if the object_user is the same as the user
            return HttpResponseForbidden('Permission Error')
        else:
            return render(request, self.template_name, {'object': object_instance})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def portfolio_list(request):
    portfolio_all = Portfolio.objects.all()
    paginator = Paginator(portfolio_all, 6)
    page = request.GET.get('page')
    portfolios = paginator.get_page(page)

    return render(request, 'portfolio/list.html', {'portfolios': portfolios})



