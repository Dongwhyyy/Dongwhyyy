from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Word, Example
from django.http import HttpResponseNotAllowed
from .forms import WordForm, ExampleForm
from django.contrib import messages

def index(request):
    word_list = Word.objects.order_by('-create_date')
    context = {'word_list': word_list}
    return render(request, 'voca/word_list.html', context)

def detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    context = {'word': word}
    return render(request, 'voca/word_detail.html', context)

def example_create(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    word.example_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('voca:detail', word_id=word.id)

def word_create(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.create_date = timezone.now()
            word.save()
            return redirect('voca:index')
    else:
        form = WordForm()
    context = {'form': form}
    return render(request, 'voca/word_form.html', context)


def word_modify(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    if request.method == "POST":
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            word = form.save(commit=False)
            word.modify_date = timezone.now()  # 수정일시 저장
            word.save()
            return redirect('voca:detail', word_id=word.id)
    else:
        form = WordForm(instance=word)
    context = {'form': form}
    return render(request, 'voca/word_form.html', context)

def word_delete(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    word.delete()
    return redirect('voca:index')

def example_modify(request, example_id):
    example = get_object_or_404(Example, pk=example_id)
    if request.method == "POST":
        form = ExampleForm(request.POST, instance=example)
        if form.is_valid():
            example = form.save(commit=False)
            example.modify_date = timezone.now()
            example.save()
            return redirect('voca:detail', word_id=example.word.id)
    else:
        form = ExampleForm(instance=example)
    context = {'example': example, 'form': form}
    return render(request, 'voca/example_form.html', context)

def example_delete(request, example_id):
    example = get_object_or_404(Example, pk=example_id)
    example.delete()
    return redirect('voca:detail', word_id=example.word.id)
