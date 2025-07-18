# Welcome to my repository for "The Farmer Was Replaced"!
## What is ["The Farmer Was Replaced"](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/)?

It is a programming game where you use a **subset** of Python to automate farming with a drone
### Limitations coding for "The Farmer Was Replaced":
#### Missing Python features in the game, and what I would've used them for:
- fStrings – Missing, which makes debugging and performance optimization harder.
- Classes – Could have helped manage grind orders, logs, and maze-solving.
- __Many__ built-in type methods, some notable mentions:
  - Almost everything string related.
  - `list.reverse`, `list.sort`, `list.index` and `list.count`

#### The game will refuse to execute any code that contains:
- Docstrings
- Type hinting
- Inlined statements (e.g., `else: return False`)

## Instructions for using the code
### Setting up the code:
1. Get the files in one of two ways
    - Clone the repository using git (recommended: directly into your save directory).
    - Download individual files and their dependencies (import statements at the top).
2. Place the ".py" files inside a save directory, along with a save file. By default on windows it will be located in:

(C:\Users\ **YourUser** \AppData\LocalLow\TheFarmerWasReplaced\TheFarmerWasReplaced\Saves\ **Yoursave** )
### Executing the code from inside the game
- Run "timed_run.py" from inside the game if you want to do a run with my code
- Run "method_tester.py" to play around with the different farming methods I've made over the past few weeks (there's quite a few, many obsolete.)
### Using the (external) tools I made
Anything located in the "tools" subdirectory will require you have Python installed and configured, you should be able to just run them without any dependencies unless specified otherwise, consult the local README for instructions.


## Known issues and future plans

- Create the timed run scripts and auto unlocking.

## Attribution
- I'm a new coder that has taken code and indeed alot of this readme from other, more intelligent, people. Full credit to the developers and original authors of the code I use. 