from django.urls import path
from .views import Berita

urlpatterns = [
    path('berita/', Berita.as_view(), name='berita'),
    # path('historical-market-cap/<int:pk>/', HistoricalMarketCapDetail.as_view(), name='historical-market-cap-detail'),
]