from django.core.cache import cache

def is_cached(cache_key):
    return cache.get(cache_key) is not None

def get_cached_results(cache_key):
    return cache.get(cache_key)

def set_cached_results(cache_key, results, timeout=600):
    cache.set(cache_key, results, timeout)
