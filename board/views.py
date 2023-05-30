from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

next_id = 4
topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ...'},
    {'id': 2, 'title': 'view', 'body': 'View is ...'},
    {'id': 3, 'title': 'model', 'body': 'Model is ...'}
]


def HTMLTemplate(article):
    global topics

    li = ''
    for topic in topics:
        li += f'<li><a href="/board/{topic["id"]}">{topic["title"]}</a></li>'

    return f'''
    <html>
        <body>
            <h1><a href="/">Django practice page</a></h1>
            <ul>{li}</ul>
            {article}
            <ul>
                <li><a href="/board/create/">create</a></li>
            </ul>
        </body>
    </html>
    '''


# Create your views here.
def index(request):
    print(f'index')
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))


@csrf_exempt
def create(request):
    print(f'create')
    if request.method == 'GET':
        article = '''
        <form action="/board/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        global next_id
        global topics

        new_id = next_id
        title = request.POST['title']
        body = request.POST['body']
        topics.append({'id': new_id, 'title': title, 'body': body})
        next_id += 1

        redirect_url = f'/board/{str(new_id)}/'

        return redirect(redirect_url)


@csrf_exempt
def update(request, id=None):
    global topics

    if request.method == 'GET':
        print(f'update/{id} GET')
        for topic in topics:
            target_id = int(id)
            if target_id == int(topic['id']):
                article = f'''
                <form action="/board/update/{topic['id']}/" method="post">
                    <p><input type="text" name="update_title" value={topic["title"]}></p>
                    <p><textarea name="update_body">{topic["body"]}</textarea></p>
                    <p><input type="submit"></p>
                </form>
                '''
                return HttpResponse(HTMLTemplate(article))

    elif request.method == 'POST':
        print(f'update POST')
        update_id = int(id)
        update_title = request.POST['update_title']
        update_body = request.POST['update_body']

        for topic in topics:
            if update_id == int(topic['id']):
                topic['title'] = update_title
                topic['body'] = update_body

        return redirect(f'/board/{update_id}')


@csrf_exempt
def delete(request):
    print(f'delete')
    global topics

    if request.method == 'POST':
        delete_id = request.POST['id']
        temp_topics = []
        for topic in topics:
            if int(topic['id']) != int(delete_id):
                temp_topics.append(topic)
        topics = temp_topics
        return redirect('/board/')


def read(request, id):
    print(f'read')
    global topics

    article = ''
    for topic in topics:
        topic_id = int(topic['id'])
        if topic_id == int(id):
            article = f'''
            <h2>{topic["title"]}</h2>
            <p>{topic["body"]}</p>
            <a href="/board/update/{topic_id}/">update</a>
            <form action="/board/delete/" method="post">
                <input type="hidden" name="id" value={topic_id}>
                <input type="submit" value="delete">
            </form>
            '''

    return HttpResponse(HTMLTemplate(article))
