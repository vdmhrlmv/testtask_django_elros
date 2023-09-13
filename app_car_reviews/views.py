from django.db.models import Count
from rest_framework import viewsets, permissions, generics, mixins, status
from rest_framework.response import Response
from .models import Country, Manufacturer, Car, Reviews
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, ReviewsSerializer, CommentCountSerializer
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework_csv.renderers import CSVRenderer


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint для просмотра и редактирования записей модели - Страна
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint для просмотра и редактирования записей модели - Производители
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint для просмотра и редактирования записей модели - Автомобили
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint для просмотра и редактирования записей модели - Отзывы
    """
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def get_permissions(self):
        # Добавление возможности выполнить метод POST без аутентификации
        if self.request.method == 'GET' or self.request.method == 'POST':
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

        return super(ReviewsViewSet, self).get_permissions()


class ExportViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint для экспорта данных в XLSX и CSV
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if 'csv' in self.request.query_params.values():
            self.renderer_classes = [CSVRenderer]
            self.filename = 'CarViewExport.csv'
        elif 'xlsx' in self.request.query_params.values():
            self.renderer_classes = [XLSXRenderer]
            self.filename = 'CarViewExport.xlsx'

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.values('car', 'car__manufacturer_id').annotate(comment=Count('comment'))
    serializer_class = CommentCountSerializer