# Digital Kulibrat Game With an AI Opponent
Kulibrat was invented by Thomas Bolander, and this repository is a software implementation
of the game in python, with the added benefit of an AI opponent.
\
\
DTU Course: 02180 Introduction to Artificial Intelligence \
Assignment: ["Board Game Assignment"](https://learn.inside.dtu.dk/d2l/lms/dropbox/user/folders_list.d2l?ou=145385) \
Due Date: 20 March 2023 at 23:59

## Rules
Details of the game rules and more can be found at:
[Kulibrat Game Rules](https://learn.inside.dtu.dk/d2l/le/content/145385/viewContent/570314/View) \
Simply put, the objective is to place pieces at your end of the board, and move them towards the
opponent's side of the board. Pieces move one step diagonally, or if facing an opponent's piece,
they can attack (take the place of) that piece. Lastly, it is possible to jump one, or multiple,
opponent pieces, if facing them in a straight line.

## How To Play
Starting the program is simply running the "main.py" file.
This can be achieved in any python editor, or by using a terminal
with command: \
`$ python main.py` (__The script does make use of the numpy library, so this should be available to your intepreter.__)
\
\
The default match is a human playing against the AI.
However, setting the config variable "CUSTOM_MATCH" in the file "main.py" will allow:
* human vs. human
* human vs. AI
* AI vs. AI

The match starts with a board print, and asks player 1 for a move.
The board is setups in terms of columns (letters a, b and c) and rows (numbers 1-4).
Moves are structured by "Column+Row to Column+Row",
e.g. "b3-c2" moves a piece from column "b" row "3" to column "c" row "2",
meaning a diagonal move upwards and to the right. The available moves are therefore:
* __\[Column+Row]__, e.g. "c4" (places a new piece at "c4")
* __\[Column1+Row1]-\[Column2+Row2]__, e.g. a4-a3 
(attacks opponent piece at "a3" with player piece at "a4")
* __\[Column+Row]-e__, e.g. b2-e
(jumps piece at "b2" over opponent's pieces and to board end, scoring a point)

## Testing
The config variables being set in the beginning of the "main.py"
file, allows for some customization of the matches being played.
* Changing the __"CUSTOM_MATCH"__ config variable allows to choose
board looks, player names, winning score and who is an AI.
* Changing the __"AI_TESTING"__ variable plays a game with two AIs
against each other, with simple, preset game settings.
* Changing the __"DEPTH_TESTING"__ variable runs multiple games
with little-to-no printing, but keeps track of which AI depth
level wins the most and by how much.
* Changing the __"SUPPRESS_PRINT"__ variable limits the amount
of information being printed about the match. This is useful
for increasing the speed of the program, or de-cluttering
the console output.
