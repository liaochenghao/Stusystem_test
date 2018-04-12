# coding: utf-8

from rest_framework import mixins, viewsets

from sleep.models import UserInfo, Questions
from sleep.serializers import UserInfoSerializer, QuestionSerializer


class UserInfoViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class QuestionViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        openid = self.request.query_params.get('openid')
        if openid:
            queryset = self.queryset.filter(user__openid=openid)
        else:
            queryset = self.queryset
        return queryset
