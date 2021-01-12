from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from user.views import check_auth_token
from post.controllers import create_thread, get_thread, delete_thread, get_all_threads, create_comment, emote, get_threads_by_topic


@api_view(['GET'])
def get_threads_view(request: Request):
    page_index = int(request.query_params.get('page_index', 0))
    threads = get_all_threads(page_index)
    response_data = {
        'status': 'OK',
        'threads': threads
    }
    return Response(response_data)


@api_view(['POST'])
def create_thread_view(request: Request):
    user = check_auth_token(request)
    if not user:
        response_data = {
            'status': 'KO',
            'message': 'Ban chua dang nhap'
        }
        return Response(response_data)

    if request.method == 'POST':
        author = user
        hashtag = request.POST.get('hashtag')
        content = request.POST.get('content')
        if create_thread(hashtag, author, content):
            response_data = {
                'status': 'OK',
                'message': 'Dang bai thanh cong',
            }
    return Response(response_data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_thread_detail_view(request: Request, thread_id: int):
    thread = get_thread(thread_id)
    if not thread:
        response_data = {
            'status': 'KO',
            'message': 'Bai viet khong ton tai'
        }

        return Response(response_data)

    if request.method == 'GET':
        response_data = {
            'thread': thread
        }
        return render(request, 'post/post_detail_page.html', response_data)

    if request.method == 'PUT':
        new_content = request.PUT.get('content')
        thread.content_set().get(pk=thread_id).value = new_content
        thread.content_set().get(pk=thread_id).save()
        response_data = {
            'status': 'OK',
            'message': 'Cap nhat bai viet thanh cong'
        }

    if request.method == 'DELETE':
        delete_thread(thread_id)
        response_data = {
            'status': 'OK',
            'message': 'Xoa bai viet thanh cong'
        }
    return Response(response_data)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def comment_view(request: Request, thread_id: int):
    if request.method == 'POST':
        user = check_auth_token(request)
        comment = request.POST.get('comment')
        if user and create_comment(thread_id, user, comment):
            return Response({
                'status': 'OK',
                'message': 'Them comment thanh cong'
            })
    return Response({
        'status': 'KO',
        'message': 'Them comment that bai'
    })


@api_view(['GET'])
def emote_view(request: Request, thread_id: int):
    user = check_auth_token(request)
    value = int(request.query_params.get('value'))
    if not value:
        return
    if user:
        if emote(thread_id, user, value):
            return Response({
                'status': 'OK',
                'message': 'Emote thành công'
            })
    else:
        return Response({
            'status': 'KO',
            'message': 'Chua dang nhap'
        })
    return Response({
        'status': 'KO',
        'message': 'Emote thất bại'
    })


@api_view(['GET'])
def search_thread_view(request: Request):
    pass


@api_view(['GET'])
def get_threads_topic_view(request: Request, topic: str):
    response_data = get_threads_by_topic(topic)
    return render(request, 'hashtag/hashtag.html', response_data)

