from rest_framework.pagination import PageNumberPagination


class ModelPagination(PageNumberPagination):
    page_size = 25
    max_page_size = 500
    page_size_query_param = "page_size"
