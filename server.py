# Echo server program
import socket
from _thread import start_new_thread
import pickle
from time import sleep
from classes.battle import Battle

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)
    print('Server started waiting for connections')
    connected = set()
    games = {}
    idCount = 0

    def thread_function(conn, p, gameId):
        global idCount
        with conn:
            print("Sendind first response")
            conn.send(pickle.dumps("Connected"))
            while True:
                try:
                    data = pickle.loads(conn.recv(2048))
                    if gameId in games:
                        game = games[gameId]
                        if not data:
                            print("Disconnected")
                            break
                        else:
                            if game.player2 == None:
                                if p == 0:
                                    game.player1 = data
                                    #player = data
                                else:
                                    game.player2 = data
                                    #player = data
                            else:
                                # Game started
                                if not game.game_running:
                                    game.game_running = True
                                    #game.rounds()
                                    game.initiative()
                                    #game.next_turn()
                                else:
                                    if game.current_fighter.move != None:
                                        game.next_turn()

                                    game.control_rounds()

                            #print("Received: ", data)
                            print("how many users: ", idCount)
                            print("Turns on game: ", gameId, " = ", game.turns)
                            print("Rounds on game", gameId," = ",game.rounds)
                            #print("Loaded game: ", game)
                            #print("Im the player: ", p)
                            conn.sendall(pickle.dumps(game))
                            sleep(4)
                    else:
                        print("Gameid not in game")
                        break
                except:
                    print("No data")
                    break

        print("Lost Connection")
        try:
            del games[p_index]
            print("Disconnected and game deleted")
        except:
            pass
        idCount -= 1

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)

        idCount += 1
        p = 0
        gameId = (idCount - 1)//2
        if idCount % 2 == 1:
            games[gameId] = Battle(gameId)
            print("Creating a new Game")
        else:
            games[gameId].ready = True
            p = 1

        start_new_thread(thread_function, (conn, p, gameId))
