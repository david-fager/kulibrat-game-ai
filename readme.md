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
The default match is a human playing against the AI.
However, setting the variable "customizeMatch" in the file "main.py" will allow:
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
