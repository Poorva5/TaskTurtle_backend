from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TaskViewSet, TaskListViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('track', TaskListViewSet, basename='task-track')
router.register('board', BoardViewSet , basename='board')
router.register('', TaskViewSet, basename='task')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('board/list', BoardViewSet.as_view({'get': 'list'})),
    path('<int:board_id>/track', TaskListViewSet.as_view({'get': 'list'}))
]
