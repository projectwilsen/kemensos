from django.urls import path
from .views import Berita, KataMasyarakatDetail

urlpatterns = [
    path('berita/', Berita.as_view(), name='berita'),
    path('kata-masyarakat/<int:id>/', KataMasyarakatDetail.as_view(), name='kata-masyarakat-detail')
]