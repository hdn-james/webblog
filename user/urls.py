from django.urls import path

from user.views import sign_up_view, sign_in_view, sign_out_view, get_user_view, profile_view


urlpatterns = [
    path('', get_user_view, name='get_user_view'),
    path('signin', sign_in_view, name='sign_in_view'),
    path('signout', sign_out_view, name='sign_out_view'),
    path('signup', sign_up_view, name='sign_up_view'),
    path('profile', profile_view, name='proflie_view')
]