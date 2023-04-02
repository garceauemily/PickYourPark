console.log('Hello world')
var socket = new WebSocket('ws://localhost:8000/ws/dashboard/');

socket.onmessage = function(e){
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);
    
    document.querySelector('#app').innerText=djangoData.value;
}