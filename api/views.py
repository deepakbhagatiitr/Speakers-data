from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Speaker
from .serializers import SpeakerSerializer
from .permissions import IsAdminOrReadOnly  

class SpeakerListCreateView(ListCreateAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAdminOrReadOnly]  

class SpeakerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    permission_classes = [IsAdminOrReadOnly]  
