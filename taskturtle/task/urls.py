from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TaskViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('board', BoardViewSet , basename='board')
router.register('', TaskViewSet, basename='task')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('board/list', BoardViewSet.as_view({'get': 'list'}))
]
