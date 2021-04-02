from django.shortcuts import render, redirect
from .models import Portfolio
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import PortfolioForm
from django.core.paginator import Paginator

class PortfolioCreateView(CreateView):
    model = Portfolio
    #fields = ['portfolio', 'title', 'content']
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


class PortfolioUpdateView(UpdateView):
    model = Portfolio
    #fields = ['portfolio', 'title', 'content']
    form_class = PortfolioForm
    template_name = 'portfolio/update.html'


def portfolio_list(request):
    portfolio_all = Portfolio.objects.all()
    paginator = Paginator(portfolio_all, 8)
    page = request.GET.get('page')
    portfolios = paginator.get_page(page)

    return render(request, 'portfolio/list.html', {'portfolios': portfolios})



