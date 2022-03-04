from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.homepage.as_view(), name='hello'),
    path('chude/', views.topic.as_view(), name='topic'),
    path('chude/education/<int:pk>/', views.newword.as_view(), name='newword'),
    path('topics/', views.GetAllTopic.as_view(), name='topics'),                #api xem và tạo chủ đề
    path('newwords/', views.GetAllNewword.as_view(), name='newwords'),          #api sửa và xóa chủ đề
    path('topics/<int:pk>/', views.UpdateDeleteTopic.as_view(), name=''),       #api xem và tạo từ mới
    path('newwords/<int:pk>/', views.UpdateDeleteNewword.as_view(), name=''),   #api sửa và xóa từ mới
    path('topic/<int:pk>/', views.GetTopic.as_view(), name=''),                 #api xem 1 chủ đề
    path('chude/education/', views.Education.as_view(), name='education'),
    path('chude/travels/', views.Travels.as_view(), name='education'),
    path('chude/history/', views.History.as_view(), name='history'),
    path('pos/', views.GetAllPos.as_view(), name='pos'),                        #api xem tất cả Pos
    path('speaking/', views.GetAllSpeaking.as_view(), name='speaking'),         #api xem tất cả Speaking
    path('listening/', views.GetAllListening.as_view(), name='listening'),      #api xem tất cả listening
    path('reading/', views.GetAllReading.as_view(), name='reading'),            #api xem tất cả reading
    path('exam/', views.GetAllExam.as_view(), name='exam'),                     #api xem tất cả exam
    path('question/', views.GetAllQuestions.as_view(), name='question'),        #api xem tất cả question
    path('grammars/', views.GetAllGrammars.as_view(), name='grammars'),         #api xem tất cả grammars
    path('addnewword/', views.AddNewword.as_view(), name='addnewword'),
    path('luyennoi/', views.speaking.as_view(), name='luyennoi'),
    path('luyennghe/', views.listening.as_view(), name='luyennghe'),
    path('luyennghe/ss/', views.listening2.as_view(), name='some'),
    path('luyendoc/', views.reading.as_view(), name='reading'),
    path('luyendoc/education/', views.ReadingEducation.as_view(), name='readingeducation'),
    path('luyendoc/travels/', views.ReadingTravels.as_view(), name='readingtravels'),
    path('luyendoc/history/', views.ReadingHistory.as_view(), name='readinghistory'),
    path('tuvung/', views.TuVung.as_view(), name='tuvung'),
    path('nguphap/', views.NguPhap.as_view(), name='nguphap'),

]