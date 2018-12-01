# maze
a python program that solves a series of mazes without any local information about those mazes
-------------------------------------------------------------------------
copyright of Franklin Zhicheng Ren, UCLA CS department
environment - python 3.6
-------------------------------------------------------------------------
This project solves a sequence of n*n mazes without being given any prior
knowledge about the structure of the maze. The communication between this
maze solver and the web server is achieved through the "get" function and
the "post" function, using the "requests" module from library. If all the
mazes are correctly solved, the program will output "FINISHED" and return
0. Otherwise it will output respective error messages. It also output the
level the player is currently at.
The program uses four helper functions - move, get_location, in_range and
recursion.
move: uses "post" function to move one step forward in the direction that
is specified by the player, and get the results of that action.
get_location: keeps track on the player's location on mazes, by analysing
the four input directions.
in_range: checks whether the player is out of bound.
recursion: recursively determines whether a path exists from a particular
point to the endpoint of the maze. It returns true if the path exists and
false otherwise.
In the main part of the program, when the game is not finished (there are
still > 0 unsolved mazes), the program gets the player's current location
and the size of the maze the player is currently at. Then, it gives calls
to the "recursion" function in order to get to the end of this particular
maze. Once the game is finished, the programs terminates. However, if any
error occurs during this solving process, the program will also terminate
and output respective error messages, such as "NONE" or "GAME_OVER".
Nov 30, 2018
-------------------------------------------------------------------------
