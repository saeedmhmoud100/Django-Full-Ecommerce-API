from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        next_page_number = self.page.next_page_number() if self.page.has_next() else None
        previous_page_number = self.page.previous_page_number() if self.page.has_previous() else None


        return Response({
            'result':self.page.paginator.count,
            'PaginationData':{
                'numberOfPages': self.page.paginator.num_pages,
                'pageNow': self.page.number,
                # 'next': self.get_next_link(),
                'next': next_page_number,
                # 'previous': self.get_previous_link(),
                'previous': previous_page_number,
            },
            'DataCountInPage':self.page_size,
            'DataCountInTisPage':len(data),
            'Data': data,
        })
