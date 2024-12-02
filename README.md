Dragon Game
A simple yet engaging arcade-style game where you control a dragon to avoid obstacles while accumulating points. The game dynamically adjusts its difficulty based on your score, offering a progressively challenging experience.

Features
Dynamic Difficulty: The game becomes harder as your score increases:
At 20 points, obstacles move faster and appear more frequently.
At 50 points, the difficulty increases further.
At 100 points, the game reaches its peak challenge.
Smooth Animations: The dragon character is animated with a series of frames for a lively appearance.
Mouse Control: Move the dragon up and down with your mouse to dodge obstacles.
Restart Mechanism: Press R to restart the game after a collision.
Gameplay
Objective: Avoid obstacles and achieve the highest score possible.
Controls: Move the dragon vertically using your mouse.
Game Over: The game ends when the dragon collides with an obstacle. A message prompts you to restart by pressing R.
Installation
Clone the Repository:

git clone https://github.com/yourusername/dragon-game.git
cd dragon-game
Install Dependencies: Ensure you have Python 3 and pygame installed. If not, install pygame using pip:

pip install pygame
Prepare Assets:

Place the following files in the same directory as the script:
dragon1.png, dragon2.png, dragon3.png, dragon4.png, dragon5.png, dragon6.png (Dragon animation frames)
obstacle.png (Obstacle image)
background.png (Background image)
Run the Game:

python dragon_game.py
File Structure
dragon-game/
├── dragon_game.py     # Main game script
├── dragon1.png        # Dragon animation frame 1
├── dragon2.png        # Dragon animation frame 2
├── dragon3.png        # Dragon animation frame 3
├── dragon4.png        # Dragon animation frame 4
├── dragon5.png        # Dragon animation frame 5
├── dragon6.png        # Dragon animation frame 6
├── obstacle.png       # Obstacle image
├── background.png     # Background image
How the Code Works
Game Initialization:

Initializes pygame, loads assets, and sets up game variables.
Dynamic Difficulty:

Adjusts obstacle_speed and obstacle_frequency based on the score to make the game progressively harder.
Async Game Loop:

The main game logic runs in an asynchronous loop, allowing for smooth frame updates and dynamic difficulty scaling.
Collision Detection:

Uses pygame.Rect to check for collisions between the dragon and obstacles.
Game Over Mechanism:

Displays a "Game Over" message and waits for the player to restart by pressing R.
Future Enhancements
Add sound effects for collisions and scoring.
Introduce power-ups or bonus items.
Implement a leaderboard to save high scores.
Provide keyboard control as an alternative to mouse input.
License
This project is open-source and available under the MIT License.

Acknowledgments
Created using the pygame library.
Designed and developed by Your Name.
