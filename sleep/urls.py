# coding: utf-8

from rest_framework.routers import SimpleRouter
from sleep.views import UserInfoViewSet, QuestionViewSet

router = SimpleRouter()
router.register('user_info', UserInfoViewSet)
router.register('question', QuestionViewSet)

urlpatterns = router.urls
