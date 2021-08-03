from flask import Flask, request
import simple_websocket, random


app = Flask(__name__)

class Player1:
    def __init__(self, color, room):
        self.color = random.choice(['white','black'])
        self.room = random.randint(1000, 9999)

class Player2:
    def __init__(self, color, room):
        self.color = color
        self.room = room
        

    def get_room(self, room):
        self.room = Player1().room


    def get_color(self, color):
        if Player1().color == 'white':
            self.color = 'black'
        elif Player1().color == 'black': 
            self.color = 'white'

@app.route('/')
def ping():
    return "It's Alive!"

@app.route('/game', websocket=True)
def game_loop():
    socket = simple_websocket.Server(request.environ)
    #Setting Game
    try:
        while True:
            socket.receive()
            set_player = 'Start Game?'
            socket.send(set_player)
            if socket.receive(600).lower() == 'yes':
                Player1()
                socket.send('Wait for player 2...')
            socket.send(set_player)
            if socket.receive(600).lower() == 'yes':
                Player2().get_room()
                Player2().get_color()
    except simple_websocket.ConnectionClosed:
        pass

    #Game Mechanics
    try:
        while True:
            move = socket.receive()
            #randomize player color
                #check if it is legal move
                    #move
                    #report ilegal move
                        #check if it is check
                            #report check
                        #check if it is checkmate
                            #Report check mate
                            # end game
                        #check if it is stalemate
                            #report stalemate
                            #end game
                    #Pass turn
            socket.send(resp)
    except simple_websocket.ConnectionClosed:
        pass
    return ''


if __name__ == '__main__':
    app.run(debug=True)

