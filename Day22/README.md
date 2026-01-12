# Pong Game (Python Turtle)

A simple two-player Pong game built using Python’s built-in `turtle` module.  
The game continues until **either player reaches 10 points**, after which the winner is announced and the game stops.

---

## Features

- Two-player gameplay (Player 1 vs Player 2)
- Smooth paddle and ball movement
- Real-time score tracking
- Game automatically stops when a player reaches 10 points
- Clean object-oriented structure

---

## Technologies Used

- Python 3
- Turtle Graphics
- Object-Oriented Programming (OOP)

---

## Project Structure

- Project22.py  (Main game loop)
- paddle.py (Paddle class)
- ball.py  (Ball class)
- scoreboard.py (Scoreboard and winner logic)

---

## Controls

### Player 1 (Left Paddle)
- Move Up: `w`
- Move Down: `s`

### Player 2 (Right Paddle)
- Move Up: `↑` (Up Arrow)
- Move Down: `↓` (Down Arrow)

---

##  Game Rules

- Each time a player misses the ball, the opponent scores 1 point.
- The first player to reach **10 points** wins.
- Once a player wins, the game stops and the winner is displayed on the screen.

---
