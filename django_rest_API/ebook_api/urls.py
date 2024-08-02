from django.urls import path
from ebook_api.views import EbookListCreateViewUsingMixin, EbookListCreateAPIView, EbookDetailsAPIView, ReviewCreateAPIView, ReviewDetailsAPIView


urlpatterns = [
    path("ebook_mixins/", EbookListCreateViewUsingMixin.as_view(), name="ebook_mixins"),

    path("ebook/", EbookListCreateAPIView.as_view(), name="ebooks"),
    path("ebook/<int:pk>/", EbookDetailsAPIView.as_view(), name="ebook_details"),

    path("ebook/<int:ebook_pk>/review/", ReviewCreateAPIView.as_view(), name="ebooks_review"),
    path("reviews/<int:pk>/", ReviewDetailsAPIView.as_view(), name="review_details"),
]