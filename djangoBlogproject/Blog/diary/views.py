from multiprocessing.dummy import current_process
from django.shortcuts import redirect, render
from .forms import PageForm
from .models import Page
from django.core.paginator import Paginator
# Create your views here.


def page_list(request):
    object_list = Page.objects.all()
    paginator = Paginator(object_list, 6)  # 모델에서 내용 갖고 오고 한 페이지에 내용 6개
    curr_page_number = request.GET.get('page')
    if curr_page_number is None:
        curr_page_number = 1
        # 처음에 메인 페이지로 접근한 상태에선 페이지 넘버가 없음
    page = paginator.page(curr_page_number)
    return render(request, 'diary/page_list.html', {'page': page})
    # return render(request, 'diary/page_list.html', {'object_list': object_list})
    # 함수형 view에선 html에 page.something 이런 양식으로 적어줘여 한다.


def page_detail(request, page_id):
    object_detail = Page.objects.get(id=page_id)
    return render(request, 'diary/page_detail.html', {'object_detail': object_detail})


def page_create(request):
    # views가 form을 html파일과 연결해주는 역할을 했다
    # post 방식의 요청이 들어오면 # 작성한 데이터를 가져와서 새로운 Page 데이터 모델을 만들고 # 데이터를 저장한 후 # 방금 작성한 상세 일기 보기 페이지로 이동합니다.
    if request.method == 'POST':
        form = PageForm(request.POST)  # 얘는 채워진 폼을 받은거다
        #           Page(
        #     title = request.POST['title'],
        #     content = request.POST['content'],
        #     feeling=request.POST['feeling'],
        #     score = request.POST['score'],
        #     dt_created=request.POST['dt_created'],
        #     ) 모델폼 적용 전에는 이런식으로 Page에서 갖고 왔었지만 모델폼 적용히면 더 간편해짐
        # new_page.is_valid()
        if form.is_valid():
            new_page = form.save()
            return redirect('page-detail', page_id=new_page.id)
        # else:
        #     return render(request, 'diary/page_create.html',{'form':paged}) 밑에랑 중복이니까 합치자
    else:
        form = PageForm()  # 비어 있는 form을 만들어주거나 유효값 검사에서 걸렸을 경우 이전에 작성한 폼을 받는다
    # PageForm을 이용해서 새로운 form을 생성하고 # 생성한 form을 전달받은 page_form 템플릿을 랜더해서 결과로 돌려줍니다.
    return render(request, 'diary/page_create.html', {'form': form})


def page_update(request, page_id):
    update = Page.objects.get(id=page_id)
    if request.method == 'POST':
        # 기존의 데이터 모델에 새로운 데이터를 설정하고
        form = PageForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('page-detail', page_id=update.id)
    else:
        form = PageForm(instance=update)
    return render(request, 'diary/page_create.html', {'form': form})


def page_delete(request, page_id):
    object = Page.objects.get(id=page_id)

    if request.method == 'POST':
        object.delete()
        return redirect('page-list')
    else:
        return render(request, 'diary/page_confirm.html', {'object': object})
