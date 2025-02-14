from django.urls import path
from .views import SpeakerListCreateView, SpeakerDetailView

urlpatterns = [
    path("speakers/", SpeakerListCreateView.as_view(), name="speaker-list"),
    path("speakers/<int:pk>/", SpeakerDetailView.as_view(), name="speaker-detail"),
]
