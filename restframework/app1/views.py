from .permissions import ReadOnlyOwner, QuestionByOwner
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import Questions, Choices


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,
                          ReadOnlyOwner,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choices.objects.all()
    serializer_class = ChoiceSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated, QuestionByOwner,)

    def perform_create(self, serializer):
        serializer.save()


choices_list = ChoiceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
choices_detail = ChoiceViewSet.as_view({
    'get': 'Retrieve',
    'put': 'Updating',
    'patch': 'partial_update',
    'delete': 'Destroy'
})

question_list = QuestionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})