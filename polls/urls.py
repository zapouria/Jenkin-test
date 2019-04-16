from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import QuestionList, QuestionDetail,ChoiceList,CreateVote,QuestionViewSet

router = DefaultRouter()
router.register('polls', QuestionViewSet, base_name='polls')

urlpatterns = [
    path("", QuestionList.as_view(), name="polls_list"),
    path("<int:pk>/", QuestionDetail.as_view(), name="polls_detail"),
    path("<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls
