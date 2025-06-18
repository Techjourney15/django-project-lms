from django.urls import path
from core.views import HomePageView,TeacherListView, TeacherCreateView,TeacherDeleteView,TeacherDetailView,TeacherUpdateView
 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('teacher/list/', TeacherListView.as_view(), name='teacher.index'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher.create'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher.detail'),
    path('teacher/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher.update'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher.delete'),
]