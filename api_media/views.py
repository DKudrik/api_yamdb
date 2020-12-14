from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Category, Comment
from .permissions import IsGetOrIsAdmin, IsGetOrPostOrAdmin
from .serializers import CategorySerializer, CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsGetOrIsAdmin]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', )

    def destroy(self, request, *args, **kwargs):
        category = get_object_or_404(Category, slug=kwargs['slug'])
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    """  A ViewSet for viewing and editing comments."""

    serializer_class = CommentSerializer
    permission_classes = [IsGetOrPostOrAdmin]
    pagination_class = PageNumberPagination
    http_method_names = [
        'get',
        'post',
        'patch',
        'delete',
    ]

    def get_queryset(self, *args, **kwargs):
        """  Returns comments of a review."""
        review_id = self.kwargs.get('review_id')
        get_object_or_404(Review, pk=review_id)
        return Comment.objects.filter(review__pk=review_id)

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        get_object_or_404(Review, pk=review_id)
        serializer.save(author=self.request.user, review_id=review_id)
