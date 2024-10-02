# ArchieDodge
Archibald’s Adventure

Overview

Welcome to Archibald’s Adventure, a fun and challenging 2D platformer game where you help Archibald jump over obstacles and avoid collisions! The game is built using Python and Pygame, featuring basic animation, sprite collision, and key game mechanics like jumping and falling.

Table of Contents

	1.	Features
	2.	Setup Instructions
	3.	Controls
	4.	Gameplay
	5.	Bash Scripts
	6.	Disclaimer
	7.	Future Enhancements
	8.	License

Features

	•	Simple Jump and Fall Mechanics: Help Archibald navigate by jumping and avoiding obstacles.
	•	Dynamic Obstacles: Randomly generated obstacles that increase in speed over time.
	•	Collision Detection: Immediate feedback when Archibald hits an obstacle, prompting a game restart.
	•	Customizable Sprites: Easily swap out the archie_0.png and obstacle0.png with your own custom sprites for a personalized experience.
	•	Score Display: A time-based score displayed on the screen during gameplay.

Setup Instructions

	1.	Clone the repository:
git clone https://github.com/yourusername/archiedodge.git
cd archiedodge

2.	Install dependencies:
Make sure you have Python and Pygame installed. If not, install Pygame with
pip install pygame


3.	Prepare the images:
Ensure that the image files archie_0.png and obstacle0.png are in the same directory as the game script. Important: Adjust the file paths on lines 110 and 201 to reflect your local system’s image paths if necessary.
	4.	Run the game:
Run the Python script to start the game

python archiedodge.py


Controls

	•	Arrow Up: Jump.
	•	Arrow Down: Fall down faster.

Gameplay

	•	Jumping: Press the Up Arrow to make Archibald jump over obstacles. The height and duration of the jump are controlled by a sinusoidal function, ensuring smooth gameplay.
	•	Obstacles: Randomly generated obstacles will move across the screen, with their speed increasing over time. Avoid hitting them!
	•	Restart: If Archibald collides with an obstacle, the game automatically resets.
