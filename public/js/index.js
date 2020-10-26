$(document).ready(() => {
    const socket = io();


    $('#btn-submit').click(() => {
        socket.emit('download', {
            url:  $('#target-url').val(),
            dest: $('#destination').val()
        });
    });
});
