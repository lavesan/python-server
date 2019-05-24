const express = require('express')
console.log('1')
const socketIO = require('socket.io')
console.log('2')
const port = 8080;

const app = express()
const server = http.createServer(app)
const io = socketIO(server)

server.listen(port, () => {
    console.log(`Conectado na porta ${port}`)
})

const socket = io()

socket.on('GET ')