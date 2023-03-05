from django.shortcuts import render
from django.http import HttpResponseRedirect


def get_name(request):
    # POST 방식이면 데이터가 담긴 제출된 폼으로 간주한다
    if request.method == 'POST':
        # request에 담긴 데이터로 클래스 폼을 생성한다
        form = NameForm(request.POST)
        # 폼에 담긴 데이터가 유효한지 체크한다
        if form.is_valid():
            # 폼 데이터가 유효하면 데이터는 cleaned_data로 복사된다
            new_name = form.cleaned_data['name']
            # 로직에 따라 추가 처리를 한다

            # 새로운 URL 로 리디렉션 시킨다
            return HttpResponseRedirect('/thanks/')
    # POST 방식이 아니라면(GET):
    # 빈 폼을 사용자에게 보여준다
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})


def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm(initial={'key': 'value'})
    return render(request, 'form_template.html', {'form': form})
