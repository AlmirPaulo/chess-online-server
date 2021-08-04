from flask import Flask, request
import simple_websocket, random, logging, pdb

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route('/')
def ping():
    return "It's Alive!"

@app.route('/game', websocket=True)
def game_loop():
    socket = simple_websocket.Server(request.environ)

    #Start Game
    players = []
    try:
        player = socket.receive(300)
        player = player.partition('/')
        players.append()
        try:
            player1 = players[-1].partition('/')
            if player1[2] == player2[2]:
                if player1[0] == 'white' and player2[0] == 'white':
                    player2_color = 'black'
                    player1_color = 'white'
                    logging.debug(player2_color, player1_color)
                   # game_mechanics()
                elif player1[0] == 'black' and player2[0] == 'black':
                   player2_color = 'white'
                   player1_color = 'black'
                   logging.debug(player2_color, player1_color)
                   # game_mechanics()
                else:
                   player1_color = player1[0]
                   player2_color = player2[0]
                   logging.debug(player2_color, player1_color)
                   # game_mechanics()
        except:
            socket.send('Waiting for a second player...')
        pdb.set_trace()

    except simple_websocket.ConnectionClosed:
        pass
    return ''


def game_mechanics():
    while True:
        move = socket.receive(600)
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

