from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from .forms import PostForm, sortForm
from django.db.models import Q
from operator import contains

def postlist1(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            child = form.save(commit=False)
            child.save()
            return redirect('file:info')
    else:
        form = PostForm()
    return render(request, 'file/post_list.html', {'form': form})


def info(request):
    PostModel = models.PostModel
    show = request.POST.get('show', 25)
    sort_by = 'username'
    # if models.sort.sortchoices == 'Name':
    #     sort_by = 'username'
    # elif models.sort.sortchoices == 'Email':
    #     sort_by = 'Email'
    user_list = PostModel.objects.order_by(sort_by)
    page = request.GET.get('page', 10)
    paginator = Paginator(user_list, show)
    try:
        PostModel = paginator.page(page)
    except PageNotAnInteger:
        PostModel = paginator.page(1)
    except EmptyPage:
        PostModel = paginator.page(paginator.num_pages)
    return render(request, 'file/Info.html',
                  {'PostModel': PostModel, 'sort_by': sort_by, 'show': show, 'sortform': sortForm})




def search(request):
    query = request.GET.get('q')
    all_data=models.PostModel.objects.all()
    data=list(all_data.values())
    resultdata=[]
    for e in data:
        if (contains(e["username"],query)) or (contains(e["Email"],query)) or (contains(e["states"],query)) or (contains(str(e["year"]),query)):
            resultdata.append(e)
    if query:
        context = {
            'PostModel': resultdata,
            'sortform': sortForm
        }
    else:
        context={
            'PostModel':all_data,
            'sortform':sortForm
        }
    return render(request, 'file/Info.html', context)


def sortdata(nlist, sorttype):
    if len(nlist) > 1:
        mid = len(nlist) // 2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        sortdata(lefthalf,sorttype)
        sortdata(righthalf,sorttype)
        i = j = k = 0
        if sorttype=="usernameatoz":
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i]["username"] < righthalf[j]["username"]:
                    nlist[k] = lefthalf[i]
                    i = i + 1
                else:
                    nlist[k] = righthalf[j]
                    j = j + 1
                k = k + 1
        elif sorttype=="usernameztoa":
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i]["username"] > righthalf[j]["username"]:
                    nlist[k] = lefthalf[i]
                    i = i + 1
                else:
                    nlist[k] = righthalf[j]
                    j = j + 1
                k = k + 1
        elif sorttype=="emailatoz":
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i]["Email"] < righthalf[j]["Email"]:
                    nlist[k] = lefthalf[i]
                    i = i + 1
                else:
                    nlist[k] = righthalf[j]
                    j = j + 1
                k = k + 1
        elif sorttype=="emailztoa":
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i]["Email"] > righthalf[j]["Email"]:
                    nlist[k] = lefthalf[i]
                    i = i + 1
                else:
                    nlist[k] = righthalf[j]
                    j = j + 1
                k = k + 1
        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return nlist


def sort(request):
    sort_by = request.GET.get('sortchoices')
    all_data=models.PostModel.objects.all()
    all_values=list(all_data.values())
    sortedlist=sortdata(all_values,sort_by)

    context = {
        'data': sortedlist,
        'sortform': sortForm
    }
    return render(request, 'file/sort.html', context)
