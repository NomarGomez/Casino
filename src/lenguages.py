lenguages = {
                "english":
                    {
                    "card_class":{},
                    "CPU_class":{
                        "play":  " has ended his turn click enter to continue \n",
                        "trail": " will trail ",
                        "capture": [" will take "," with "]
                    },
                    "player_class":{
                        "displayhand": "Hand \n",
                        "displayoffhand": "\nOff-hand\n",
                        "display": "Cards captured: ",
                        "inputokeye": "Unable to find the card. Reason: ",
                        "inputtokeye1": "is out of range, please follow the instructions and try again ",
                        "inputtokeye2": "isn't a whole number, please follow the instructions and try again ",
                        "help": "Drop or Trail: \n you will select one card to drop on the table it can't be a card with the same rank with one in the table \nCapture:\n First you will select the card on your hand that you want on the second input you select the card or cards that you want to capture notice that the card of your hand must be equal to the sum of the card or cards that you select on the table\nHelp:\n displays this string\nFlip:\n this is a hidden command used when you're playing with friends it will encode your cards so you're able to tell your friends so they stop looking if you want to see your cards",
                        "dropinput": "Select wich card do you want to drop \n",
                        "droperror": ["Unable to drop", "Reason ", " have the same value"],
                        "captureinput1": "Select wich card on your hand do you want to use \n",
                        "captureinput2": "Select wich card, cards or build do you want to capture \n",
                        "captureerror1":"The value of the card in your hand isn't equal to the value of the targets in the table, please follow instructions and try again ",
                        "captureerror2": "You selected two or more times the same card, please follow instructions and try again ",
                        "commands": ["help", "drop","trail","capture","flip"],
                        "action": " is your turn, select an action (help, drop, trail or capture):  \n",
                        "actionerror": " isn't a valid action, please type 'help' to see the actions available "

                    },
                    "table_class":{
                        "blankscoreboard": "Players doesn't have score yet",
                        "table": "Table \n",
                        "round": "Round: ",
                        "scoreboard": "Scoreboard:\n",
                        "nextbatch": ["The batch has finished, click enter to the table start giving the scores","Calculating players scores"],
                        "scores":  [" Scored a point. Reason: ", " Scored two points. Reason: ",
                                    " Scored three points. Reason: Owns most cards","Noobody gets points for owning most cards",
                                    " Scored a point. Reason: Owns most spades","Noobody gets points for owning most spades",
                                    "Here are the scores click enter to continue"],
                        "gameover": ["The game has ended click enter to view results","Winner is ",
                                     "Scoreboard: \n ","Thanks for playing!"]

                    },
                    "menu":{
                            "lobby": 
                                {
                                "choices": ["play","help","quit"],
                                "input": "Play (0) \nHelp (1) \nExit (2) \n \nSelect by writing down which one do you wich to use \n",
                                "exit_message": "Closing program, thanks for playing!",
                                },
                            "toPlay":
                                {
                                "ask": "How many CPU do you want to play with \n",
                                "ask2": "How many real players (Humans) do you want to play with \n",
                                "ask3": "Do you want to play singleplayer (0) or multiplayer (1) write down your answer or the number in the parentheses\n",
                                "error": " Previus inputs are out of range",
                                "error2":" Previus inputs were not numbers",
                                "gamemodes": ["singleplayer", "multiplayer"]
                                },
                            "howtoplay": "For navigating the menu just write down what you want to click or the number in the parentheses \nIf you select Play it will ask you what mode you want play on it Singleplayer means that you will play with machines \nhowever multiplayer means you will play with your friends on the same computer,\nwhen you're playing use the command help to get in game help. \n",
                            "help_exit_message": "Click enter to go back to menu",
                            "exit_message": "Thanks for playing! Closing program"
                            }
                    },
                "spanish":{
                    "card_class":{},
                    "CPU_class":{
                        "play":  " termino su turno presiona enter para continuar \n",
                        "trail": " Va a soltar ",
                        "capture": [" Va a tomar "," con "]
                    },
                    "player_class":{
                        "displayhand": "Mano\n",
                        "displayoffhand": "\nFuera de la mano\n",
                        "display": "Cartas capturadas ",
                        "inputokeye": "No se pudo encontrar la carta. Razon: ",
                        "inputtokeye1": "Esta fuera de rango por favor siga las instrucciones e intente de nuevo",
                        "inputtokeye2": "No es un numero entero, por favor siga las instrucciones e intente de nuevo ",
                        "help": "Soltar o votar: \nVas a seleccionar una carta de tu mano para soltarla en la mesa ojo no puedes soltar una carta que tenga el mismo valor de una en la mesa \nCapturar:\nPrimero seleccionas la carta de tu mano que quieras utilizar para capturar las cartas de la mesa, la suma de las cartas de la mesa deben dar el mismo valor que la carta de tu mano\nAyuda:\n salta este mensaje\nVoltear:\n esta accion volteara las cartas a tu conveniencia para que puedas ver o no ver (Usado en multijugador)",
                        "dropinput": "Selecciona que carta quieres soltar \n",
                        "droperror": ["No se pudo soltar", "Razon ", " tienen el mismo valor"],
                        "captureinput1": "Selecciona que cartas de tu mano quieres usar para capturar\n",
                        "captureinput2": "Selecciona la carta o cartas que quieres capturar\n",
                        "captureerror1":"El valor de la carta de tu mano no es el mismo que el de la mesa, por favor siga las instrucciones e intente de nuevo",
                        "captureerror2": "Seleccionaste una o dos veces la mismas cartas, por favor siga las instrucciones e intente de nuevo ",
                        "commands": ["ayuda", "soltar","votar","capturar","voltear"],
                        "action": " es tu turno, selecciona una accion (ayuda, soltar, votar o capturar):  \n",
                        "actionerror": " no es una accion valida, porfavor utiliza 'ayuda' para ver las acciones disponibles "

                    },
                    "table_class":{
                        "blankscoreboard": "Los jugadores no tienen puntos aun",
                        "table": "Mesa \n",
                        "round": "Ronda: ",
                        "scoreboard": "Marcador:\n",
                        "nextbatch": ["La hornada termino, presiona enter para calcular los puntos ","Calculando los puntos de los jugadores..."],
                        "scores":  [" Obtuvo un punto, Razon: ", " Obtuvo dos puntos, Razon",
                                    " Obtuvo tres puntos, Razon: tiene la mayoria de cartas ","Nadie consigue puntos por tener la mayoria de cartas",
                                    " Obtuvo un punto. Razon: Tiene pi ","Nadie obtuvo puntos por tener mas pi",
                                    "Aqui esta el marcador presiona enter para continuar"],
                        "gameover": ["El juago a acabado presiona enter para ver el marcador","El ganador es ",
                                     "Marcador: \n ","Gracias por jugar"]

                    },
                    "menu":{
                            "lobby": 
                                {
                                "choices": ["Jugar","Ayuda","Salir"],
                                "input": "Jugar (0) \nAyuda (1) \nSalir (2) \n \nSelecciona escribiendo cual de las anteriores quieres realizar \n",
                                "exit_message": "Cerrando el programa gracias por jugar!",
                                },
                            "toPlay":
                                {
                                "ask": "Con cuantas maquinas quieres jugar \n",
                                "ask2": "Cuantos jugadores reales van a jugar? \n",
                                "ask3": "Quieres jugar Solitario (0) o Multijugador (1) escribe para seleccionar (Puedes usar los numeros de los entreparentesis)\n",
                                "error": " Las entradas anteriores estan fuera de rango",
                                "error2":" Las entradas anteriores no eran numeros",
                                "gamemodes": ["solitario", "multijugador"]
                                },
                            "howtoplay": "Para navegar por el menu escribe o usa los numeros de los parentesis para seleccionar\nSi seleccionas jugar te preguntara que si quieres jugar Solicario que significa que seras capas de jugar con maquinas\nsin embargo multijugador significa que podras jugar con amigos en la misma computadora,\nCuando estes jugando utiliza el comando \"ayuda\" para direcciones en el juego \n",
                            "help_exit_message": "Presiona enter para volver al menu",
                            "exit_message": "Gracias por jugar!"
                            }
                    },
                "start": "Select which lenguage you want to use / Seleccione el lenguage que quiere usar \n English / Spanish \n"
                }

if __name__ == "__main__":
    pass