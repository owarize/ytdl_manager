import os

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


# ---------------------------------------------------------------------------------------------------- SOCKET.IO
@sio.on('download')
def download(sid, data):
    print(data['url'], '->', data['dest'])


# ---------------------------------------------------------------------------------------------------- MAIN
def main():
    eventlet.wsgi.server(eventlet.listen(('', port)), app)


if __name__ == '__main__':
    main()
