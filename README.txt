# 4 Pics & 1 Word - Tech Edition 🚀
### Final Project | Code in Place 2026

Welcome to **4 Pics & 1 Word - Tech Edition**, an interactive puzzle game built completely in Python using `Tkinter` and `Pillow`. 

The game challenges players to find the common link between four images. Since this edition is dedicated to the tech world, all answers are core concepts of programming, networking, and computing!

---

## 2. Features

* **Tech-Themed Levels:** 5 challenging levels featuring concepts like `BUG`, `CLOUD`, `KEYBOARD`, `NETWORK`, and `LOOP`.
* **Smart Hint System:** Players get 3 unique hints per level. The game dynamically analyzes the answer and isolates unique letters so clues **never repeat** during the same level.
* **Modern UI/UX Design:** Dark-mode aesthetic (`#041b3f`) with custom responsive layouts, flat styled buttons, and active hover state cursors.
* **Smart Window Positioning:** The application automatically calculates your monitor's resolution on startup to center the game window perfectly on any screen.
* **Flexible Inputs:** Fully sanitized text inputs (ignores accidental spaces and case-sensitivity) and supports pressing the `Enter` key to submit answers quickly.

---

## 3. Project Structure

```text
├── main.py                 # The core game application script
├── requirements.txt        # Third-party dependencies (Pillow)
└── img/                    # Asset directory organized by level
    ├── nivel_1/            # Images for Level 1 (BUG)
    ├── nivel_2/            # Images for Level 2 (CLOUD)
    ├── nivel_3/            # Images for Level 3 (KEYBOARD)
    ├── nivel_4/            # Images for Level 4 (NETWORK)
    └── nivel_5/            # Images for Level 5 (LOOP)
```

## 4. Installation & Setup
Follow these quick steps to set up and run the game locally:

Prerequisites
Make sure you have Python 3.x installed on your computer.

Step-by-Step Installation

1. Clone the repository:

Bash
   git clone [https://github.com/gpinedaoviedo/Game-4-Pics-1-Word](https://github.com/gpinedaoviedo/Game-4-Pics-1-Word)
   cd Game-4-Pics-1-Word

2. Install dependencies:
This project relies on Pillow for high-quality image scaling and handling within Tkinter. Install it via pip:

Bash
   pip install -r requirements.txt

3. Run the Game:
Execute the main python script to launch the interface:

Bash
   python main.py


## 5. How to Play

1. Look closely at the 4 images presented on the screen.

2. Figure out the common computer-science or technology concept connecting them.

3. Type your answer in the central input field and click Send (or simply press the Enter key).

4. Stuck? Click the Hint button! It will tell you the length of the word or reveal a unique letter contained in the answer. Use them wisely—you only get 3 hints per level!

## 6. License
This project is licensed under the MIT License - see the LICENSE file for details.

Thank you to the Stanford Code in Place team, section leaders, and community for an amazing learning journey!
