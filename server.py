from flask import Flask, request
import simple_websocket, random, logging, pdb

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


class Database:
    def __init__(self):
        self.database = ['....']

    def include(self, data):
        self.database.append(data)

    def remove(self, data):
        self.database.pop(data)


class Network:
    def __init__(self):
        self.connect = simple_websocket.Server(request.environ) 

    def recv(self):
        return self.connect.receive()

    def send(self, data):
        return self.connect.send(data)



players = Database()

@app.route('/')
def ping():
    return "It's Alive!"

@app.route('/game', websocket=True)
def game_loop():
    global socket
    socket = Network()

    #Start Game
    player = socket.recv()
    player2 = player.partition('/')
    for p in players.database:
        if p == '....':
            pass
        else:
            player1 = p
            try:
                if player1[2] == player2[2]:
                    if player1[0] == 'white' and player2[0] == 'white':
                        player2_color = 'black'
                        player1_color = 'white'
                        print(player2_color, player1_color)
                        game_mechanics(player1_color, player2_color)
                    elif player1[0] == 'black' and player2[0] == 'black':
                        player2_color = 'white'
                        player1_color = 'black'
                        print(player2_color, player1_color)
                        game_mechanics(player1_color, player2_color)
                    else:
                        player1_color = player1[0]
                        player2_color = player2[0]
                        print(player2_color, player1_color)
                        game_mechanics(player1_color, player2_color)
                else:
                    socket.send('Wait for a second Player...')


            except simple_websocket.ConnectionClosed:
                pass
    
    if any(i[2] == player[2] for i in players.database):
        socket.send('We already have this room. Please, choose other name for your room.')
    else:
        players.include(player2)
    # pdb.set_trace()
    return ''


def game_mechanics(color1, color2):
    while True:
        global socket
        move = socket.recv()
        resp = f'{color1}: {move}'
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

if __name__ == '__main__':
    app.run(debug=True)

