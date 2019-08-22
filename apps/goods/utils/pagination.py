from rest_framework.pagination import PageNumberPagination


class GoodsListPaginator(PageNumberPagination):
    """
    分页
    """
    page_size = 10
    page_query_param = 'p'
    page_size_query_param = 'len'
    max_page_size = 100