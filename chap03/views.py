from django.http import HttpResponse


def current_datatime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s</body></html>' % now
    return HttpResponse(html)
