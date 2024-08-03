from django.urls import path
from .views import search, spam, contact_detail

# These URLs are now relative to "/user/"
urlpatterns = [
    path('', search.SearchContactsView.as_view(), name='search'),
    path('<int:contact_id>/spam', spam.SpamView.as_view(), name='mark_spam'),
    path('<int:contact_id>', contact_detail.ContactDetailView.as_view(), name='contact_details'),

]


