from django.views.generic.base import TemplateView
from django.apps import apps

# ---TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['app_list'] = ['polls','books']
        dictVerbose = {}
        for app in apps.get_app_configs(): #1
            if 'site-packages' not in app.path: #2
                dictVerbose[app.label]=app.verbose_name#3
        context['verbose_dict'] = dictVerbose#4
        return context