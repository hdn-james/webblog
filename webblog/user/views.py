from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from user.controllers import sign_in, sign_up, sign_out, get_user_by_token, get_user_detail

# Create your views here.


def check_auth_token(request: Request):
    auth_token = request.COOKIES.get('auth_token')
    if auth_token:
        user = get_user_by_token(auth_token)
        if user:
            return user
    return None


@api_view(['GET'])
def get_user_view(request: Request):
    user = check_auth_token(request)
    if user:
        if request.is_ajax():
            response_data = {
                'status': 'OK',
                'message': 'Logged-in',
                'username': user.username
            }
            return Response(response_data)
        else:
            response_data = get_user_detail(user)
            return render(request, 'wall/wall.html', response_data)
    response_data = {
        'status': 'KO',
        'message': 'Not Logged-in',
    }
    return Response(response_data)


@api_view(['POST'])
def sign_up_view(request: Request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if sign_up(username, password):
        auth_token = sign_in(username, password)
        response_data = {
            'status': 'OK',
            'message': 'Account created',
        }
        response = Response(response_data)
        response.set_cookie('auth_token', auth_token,
                            max_age=60 * 60 * 24 * 30)
    else:
        response_data = {
            'status': 'KO',
            'message': 'Account existed',
        }
        response = Response(response_data)
    return response


@api_view(['POST'])
def sign_in_view(request: Request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    auth_token = sign_in(username, password)
    if auth_token:
        response_data = {
            'status': 'OK',
            'message': 'Logged-in',
            'password': password
        }
        response = Response(response_data)
        response.set_cookie('auth_token', auth_token,
                            max_age=60 * 60 * 24 * 30)
    else:
        response_data = {
            'status': 'KO',
            'message': 'Loggin fail'
        }
        response = Response(response_data)
    return response


@api_view(['GET'])
def sign_out_view(request: Request):
    user = check_auth_token(request)
    if user:
        sign_out(request.COOKIES.get('auth_token'))
    response = redirect('home')
    response.delete_cookie('auth_token')
    return response


@api_view(['GET'])
def profile_view(request: Request):
    user = check_auth_token(request)
    if user:
        response_data = {

        }
        return render(request, 'user/edit_profile.html')
    else:
        return Response({
            'status': 'KO',
            'message': 'Not Logged-in'
        })
