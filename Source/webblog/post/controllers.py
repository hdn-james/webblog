from post.models import Thread, Content, Emote


def get_all_threads(page_index: int):
    start = page_index * 5
    end = start + 5
    threads = list(Thread.objects.filter(
        parent_thread__isnull=True)[start:end])
    res = []
    for thread in threads:
        res.append(get_thread_detail(thread))
    return res


def get_thread_detail(thread: Thread):
    contents = Content.objects.filter(thread=thread)
    emotes = Emote.objects.filter(thread=thread)
    vote_count = 0
    for emote in emotes:
        vote_count += 1 if emote.type == 'Like' else -1
    res = {
        'id': thread.id,
        'author': thread.author.username,
        'created_day': thread.created_day,
        'vote_count': vote_count,
        'hashtag': thread.hashtag,
        'contents': [
            {
                'type': content.type,
                'value': content.value
            } for content in contents
        ]
    }
    if not thread.parent_thread:
        comments = Thread.objects.filter(parent_thread=thread)
        res['comments'] = [
            get_thread_detail(comment) for comment in comments
        ]
    return res


def get_thread(id: int):
    try:
        thread = Thread.objects.get(id=id)
        return get_thread_detail(thread)
    except Thread.DoesNotExist:
        return None


def create_thread(hashtag: str, author, content: str):
    new_thread = Thread(hashtag=hashtag, author=author)
    new_thread.save()
    thread_content = Content(thread=new_thread, type='Text', value=content)
    thread_content.save()
    return new_thread


def delete_thread(id: int):
    Thread.objects.filter(id=id).delete()
    return


def create_comment(thread_id, user, comment: str):
    new_thread = Thread(author=user, parent_thread_id=thread_id)
    new_thread.save()
    thread_content = Content(thread=new_thread, type='Text', value=comment)
    thread_content.save()
    return True


def emote(thread_id, user, value):
    try:
        thread = Thread.objects.get(id=thread_id)
        type = 'Like' if value == 1 else 'Unlike'
        try:
            emote = Emote.objects.get(thread=thread, user=user)
            if emote.type != type:
                emote.delete()
                return True
        except Emote.DoesNotExist:
            emote = Emote(thread=thread, user=user, type=type)
            emote.save()
            return True
    except Thread.DoesNotExist:
        return False
    return False


def get_threads_by_topic(topic: str):
    threads = Thread.objects.filter(
        hashtag__search=topic, parent_thread__isnull=True)
    return {
        'topic': topic,
        'threads': [
            get_thread_detail(thread) for thread in threads
        ]
    }
