from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.view.generic import TemplateView


class MyView(View):
    def get(self, request):
        # 뷰 로직 작성
        return HttpResponse('result')


class BookListView(ListView):
    models = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        # RFC 1123 date 포맷
        response['Last-Modified'] = last_book.publication_date.strftime(
            '%a, %d %b %Y %H:%M%S GMT')


class AboutView(TemplateView):
    template_name = "about.html"


class MyFormView(View):
    form_class = MyForm
    initial = {'key': value}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})


class MyFormv(FormView):
    form_class = MyForm
    template_name = 'form_template.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)
