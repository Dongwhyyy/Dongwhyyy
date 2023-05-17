from django.urls import path
from . import views

app_name='voca'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:word_id>/', views.detail, name='detail'),
    # url 매칭시 필요
    path('word/modify/<int:word_id>/', views.word_modify, name='word_modify'),
    # 단어 및 뜻 수정 시
    path('example/create/<int:word_id>/', views.example_create, name='example_create'),
    # 예문 작성 시
    path('word/create/', views.word_create, name='word_create'),
    # 단어 및 뜻 작성 시
    path('word/delete/<int:word_id>/', views.word_delete, name='word_delete'),
    # 단어 및 뜻 삭제 시
    path('example/delete/<int:example_id>/', views.example_delete, name='example_delete'),
    # 예문 삭제 시
]