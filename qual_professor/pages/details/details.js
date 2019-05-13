const http = require('http')
const express = require('express')
const socketIO = require('socket.io')
const port = 8080;

const app = express()
const server = http.createServer(app)
const io = socketIO(server)

server.listen(port, () => {
    console.log(`Conectado na porta ${port}`)
})

const socket = io()

socket.on('GET ')