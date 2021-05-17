from django.urls import path

from post.views import get_threads_view, create_thread_view, get_thread_detail_view, comment_view, emote_view, \
    search_thread_view, get_threads_topic_view

urlpatterns = [
    path('', get_threads_view, name='get_threads_view'),
    path('create', create_thread_view, name='create_thread_view'),
    path('<int:thread_id>', get_thread_detail_view, name='get_thread_detail'),
    path('<int:thread_id>/comment', comment_view, name='comment_view'),
    path('<int:thread_id>/emote', emote_view, name='emote_view'),
    path('search', search_thread_view, name='search_thread'),
    path('topic/<str:topic>', get_threads_topic_view, name='get_threads_topic')
]
