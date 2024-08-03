from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from functools import wraps

from ..models import Contacts
from ..serialisers import ContactSerializer
from .search_cache import is_cached, set_cached_results, get_cached_results

class SearchContactsPagination(PageNumberPagination):
    page_size = 10  # Default page size

def with_pagination_and_cache(cache_key_prefix):
    def decorator(func):
        @wraps(func)
        def wrapper(self, query):
            cache_key = f"{cache_key_prefix}-{query}"
            if is_cached(cache_key):
                cached_results = get_cached_results(cache_key)
                return Response(cached_results, status=status.HTTP_200_OK)

            results = func(self, query)
            paginator = SearchContactsPagination()
            paginated_results = paginator.paginate_queryset(results, self.request)
            serialized_results = ContactSerializer(paginated_results, many=True).data
            set_cached_results(cache_key, serialized_results, timeout=600)

            return paginator.get_paginated_response(serialized_results)
        return wrapper
    return decorator

class SearchContactsView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        name = request.GET.get('name')
        phone_no = request.GET.get('phone_no')

        if name and phone_no:
            return Response({'status': False, 'error': 'Only one query parameter (name or phone_no) allowed'}, status=status.HTTP_400_BAD_REQUEST)
        
        if name:
            return self.search_by_name(name)

        if phone_no:
            return self.search_by_phone_number(phone_no)
        
       
        return Response({'status': False,'error': 'Missing search query (name or phone_no)'}, status=status.HTTP_400_BAD_REQUEST)

    @with_pagination_and_cache(cache_key_prefix="search_results_name_")
    def search_by_name(self, name):
        contacts = Contacts.objects.filter(
            Q(name__startswith=name) |
            (Q(name__icontains=name) & ~Q(name__startswith=name))
        ).order_by('name')

        return contacts

    @with_pagination_and_cache(cache_key_prefix="search_results_phone_")
    def search_by_phone_number(self, phone_no):
        contacts = Contacts.objects.filter(phone_no=phone_no)
        if contacts.filter(is_registered=True).exists():
            contacts = contacts.filter(is_registered=True)  
        
        return contacts
