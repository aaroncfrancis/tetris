
<h1>
Tetris Game
</h1>

<h2>
Description
</h2>
Tetris is a classic puzzle video game that challenges players to manipulate falling blocks to create complete lines and clear them from the game board. In this project, I have rebuilt the original Tetris game using Python and the Pygame library, while adding my own custom features such as custom drawn blocks, music, and personalized speed preferences.


<h2>Mechanics</h2>
The Tetris game follows the classic gameplay mechanics, including:
<ul>
<li>
Falling Tetrominoes: Tetrominoes are the different shapes of the blocks that fall from the top of the game board. The player can rotate and move these blocks to fit them into the empty spaces on the board. (Up, Down, Left, Right)
</li>
<li>
Clearing Lines: When a horizontal line is completely filled with blocks, it is cleared, and the player earns points. The game becomes more challenging as the speed of the falling Tetrominoes increases over time.
</li>
<li>
Game Over: The game ends when the stack of blocks reaches the top of the game board, and the player is unable to clear lines.
</li>
<li>
Hold Piece: You can hold a piece and reuse it at any time. It will replace the current tetromino on the board. (L_Shift)
</li>
</ul>

<h2>Learning Process</h2>
I would like to acknowledge <a href="https://www.youtube.com/@CoderSpaceChannel">Coder Space</a> for providing the tutorial that served as the foundation for my project. I have modified and rewritten the code to learn and add my own custom features to make it unique and tailored to my learning objectives.

<h3>The main objective of this project was to get a deep dive into OOP in Python and the most fun way to do this was to develop a game.</h3> 
<ul>
The Tetris game project utilizes four classes:
<li>
App: This class manages the game loop, user input, and game states. It controls the overall flow of the game.
</li>
<li>
Tetris: This class represents the main game logic, including the game board, Tetrominoes, and collision detection.
</li>
<li>
Tetrominoes: This class defines the different shapes of the blocks (Tetrominoes) and their behavior, such as rotation, movement, hold, etc.
</li>
<li>
Blocks: This class represents the individual blocks that make up the Tetrominoes. It handles their position, movement, and drawing etc.
</li>
</ul>

<h3>Features</h3>
<ul>
<li>
Custom Drawn Blocks: I have created my own custom blocks using Pygame's drawing functions, giving the game a unique visual style.
</li>
<li>
Music: I have added background music to enhance the gaming experience and make it more enjoyable. Hold on Tight by Aespa 
Personalized Speed Preferences: I have implemented speed preferences that can be adjusted by the player, allowing them to customize the game's difficulty level to their liking.
</li>
</ul>

<h2>Dependencies</h2>
This project is built using Python and the Pygame library. Pygame is a powerful library for creating 2D games in Python and provides functions for handling game events, drawing graphics, playing sounds, and more.
To run this project, you will need to install Pygame.

<h2>How to Run</h2>
To run the Tetris game, follow these steps:
<ol>
<li>
Install Pygame using pip or conda, as mentioned in the Dependencies section.
</li>
<li>
Clone or download the project files to your local machine.
</li>
<li>
Open the main Python file, and run it using a Python interpreter or an IDE.
</li>
<li>
Play the game using the keyboard controls to move and rotate the Tetrominoes, clear lines, and earn points.
</li>
<li>
Customize the game speed preferences to adjust the difficulty level according to your liking.
</li>
<li>
Enjoy playing your personalized version of Tetris with custom drawn blocks and music!
</ol>

<h2>Conclusion</h2>
This project has allowed me to improve my skills in using OOP classes and composition as well as the overall the fundamental principles of OOP. I have also learned more in depth about how to use Pygame's functionalities for handling game events, graphics, and sound, enhancing my knowledge of game development. 
<br>
<br>
Through this project, I have gained confidence in my ability to learn and apply new concepts in programming, take notes to track my changes, and make a project unique and personalized. This experience has been invaluable in furthering my understanding and proficiency in Python and OOP, setting a solid foundation for my future projects and endeavors. (OOP)
