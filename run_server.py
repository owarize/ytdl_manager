import json
import os
import redis

import eventlet
import socketio


# ---------------------------------------------------------------------------------------------------- SERVER INIT
static_files = {
    '/':            'pages/index.html',
    '/js/index.js': 'public/js/index.js'
}

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files=static_files)

port = 3000
if 'PORT' in os.environ.keys():
    port = int(os.environ['PORT'])


# ---------------------------------------------------------------------------------------------------- REDIS
redis_url = ''

if 'REDIS_URL' in os.environ.keys():
    redis_url = os.environ['REDIS_URL']
else:
    config    = json.load(open('config.json'))
    redis_url = config['REDIS_URL']

red = redis.from_url(redis_url)


# ---------------------------------------------------------------------------------------------------- SOCKET.IO
@sio.on('download')
def download(sid, data):
    print(data['url'], '->', data['dest'])


# ---------------------------------------------------------------------------------------------------- MAIN
def main():
    eventlet.wsgi.server(eventlet.listen(('', port)), app)


if __name__ == '__main__':
    main()
