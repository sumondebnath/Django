from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from ebook_api.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from ebook_api.api.paginations import SmallSetPagination
from ebook_api.models import Ebook, Review
from ebook_api.serializers import EbookSerializer, ReviewSerializer

# Create your views here.



class EbookListCreateViewUsingMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class EbookDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer



class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = generics.get_object_or_404(Ebook, pk=ebook_pk)

        review_author = self.request.user

        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this Ebook!.")
        
        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]