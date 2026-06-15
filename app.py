import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# 1. DATA
NIVELES = [
    {
        "images": ["img/nivel_1/1.jpg", "img/nivel_1/2.jpg", "img/nivel_1/3.jpg", "img/nivel_1/4.jpg"],
        "answer": "BUG"
    },
    {
        "images": ["img/nivel_2/1.jpg", "img/nivel_2/2.jpg", "img/nivel_2/3.jpg", "img/nivel_2/4.jpg"],
        "answer": "CLOUD"
    },
    {
        "images": ["img/nivel_3/1.jpg", "img/nivel_3/2.jpg", "img/nivel_3/3.jpg", "img/nivel_3/4.jpg"],
        "answer": "KEYBOARD"
    },
    {
        "images": ["img/nivel_4/1.jpg", "img/nivel_4/2.jpg", "img/nivel_4/3.jpg", "img/nivel_4/4.jpg"],
        "answer": "NETWORK"
    },
    {
        "images": ["img/nivel_5/1.jpg", "img/nivel_5/2.jpg", "img/nivel_5/3.jpg", "img/nivel_5/4.png"],
        "answer": "LOOP"
    }
]

# 2: LOGIC y VARIABLES
current_level = 0
images_tk_refs = [] # kept to prevent garbage collection
hints_available = 3
current_hints = []


def load_images():
    global current_level, images_tk_refs, hints_available, current_hints
    
    # Verificate if the game was completed
    if current_level >= len(NIVELES):
        messagebox.showinfo("Congratulations!!", "You've completed all levels!", parent=window)
        window.destroy()
        return
    
    # Load the images of the current level and update the title of the level
    level = NIVELES[current_level]
    label_title.config(text=f"LEVEL {current_level + 1} - {len(NIVELES)}")
    entry_answer.delete(0, tk.END)
    
    # Reset the hints available for each level
    hints_available = 3    
    btn_hint.config(text=f"{hints_available} Hint") # Update the button text to reflect the reset hints available

    # Create the hints for the current level
    word = level["answer"]
    current_hints = [f"The answer has {len(word)} letters."]
    
    unique_letters = list(set(word))
    random.shuffle(unique_letters)
    
    # Add hints for each unique letter in the answer, but only if there are hints available
    for letter in unique_letters:
        current_hints.append(f"The answer has the letter: {letter}")

    # clear all refs of the images
    images_tk_refs.clear()
    
    # load & resized the 4 images with PIllow
    for i in range(4):
        try: 
            # open the image from the file
            img_original = Image.open(level["images"][i])
            # Re-size into a new size each image
            img_resized = img_original.resize((180,180))
            # Change the extension into one that tkinter can understand
            img_tk = ImageTk.PhotoImage(img_resized)
            # Save the refs in the global variable
            images_tk_refs.append(img_tk)
            # move the image to the widget of the correct window
            labels_images[i].config(image=img_tk)
        except FileNotFoundError:
            print(f"Error: image {level['images'][i]} not found.")


# 3. FUNCTIONS
def answer_validation():
    global current_level
    
    # Get the answer of the user and compare it with the correct answer of the level, ignoring spaces and case sensitivity
    try_user = entry_answer.get().strip().upper()
    correct_answer = NIVELES[current_level]['answer'].strip().upper()
    
    if try_user == correct_answer:
        messagebox.showinfo("¡Correct!", "Next level", parent=window)
        current_level += 1
        load_images()
    else: 
        messagebox.showinfo("¡Incorrect!", "Try again", parent=window)


def show_hint():
    global hints_available, current_hints
        
    if hints_available <= 0 or not current_hints:
        messagebox.showinfo("Hints", "No hints available or you chose not to reveal a clue.", parent=window)
        return

    option_2 = messagebox.askyesno("Hint", "Do you want to reveal a clue?", parent=window)

    if option_2:        
        reveal_hint = random.choice(current_hints)
        messagebox.showinfo("Hints", reveal_hint, parent=window)
        
        current_hints.remove(reveal_hint) # Remove the revealed hint from the list of available hints
        
        # Reduce the number of hints
        hints_available -= 1
        btn_hint.config(text=f"{hints_available} Hint")
        

# 4. INTERFACE
window = tk.Tk()
window.title("4 Pics & 1 Word - Code In Place 2026")
window.geometry("470x620")
window.configure(bg="#041b3f")

# Title by level
label_title = tk.Label(window, text="", font=("Arial", 16, "bold"), bg="#041b3f", fg="#f4f6f9")
label_title.pack(pady=15)

# images conteiner
frame_square = tk.Frame(window, bg="#15315E")
frame_square.pack()

# create 4 empty spaces (Label)
labels_images = []
positions = [(0,0), (0,1), (1,0), (1,1)]

# Create a grid of 2x2 for the images
for row, column in positions:
    lbl = tk.Label(frame_square, bd=0, highlightbackground="#f4f6f9", highlightthickness=1)
    lbl.grid(row=row, column=column, padx=8, pady=8)
    labels_images.append(lbl)
    
# Text entry for the answer
entry_answer = tk.Entry(window,  font=("Arial", 14, "bold"), bd=1, bg="#f4f6f9", fg="#0C3474", justify="center", relief="solid", highlightbackground="#01378f", highlightthickness=2)

entry_answer.pack(pady=15, ipady=6)
entry_answer.bind("<Return>", lambda event: answer_validation())

# Button of Send/Verify answer
btn_verify = tk.Button(
    window, 
    text="Send", 
    font=("Arial", 12, "bold"), 
    bg="#2ecc71", 
    fg="black", 
    relief="flat",
    activebackground="#27ae60",
    activeforeground="#f4f6f9",
    cursor="hand2",
    width=10,
    pady=4,
    command=answer_validation
    )

# Button of Hint
btn_hint = tk.Button(
    window, 
    text=f"{hints_available} Hint", 
    font=("Arial", 12, "bold"), 
    bg="#b3b3b3", 
    fg="black", 
    relief="flat",
    activebackground="#999999",
    activeforeground="black",
    cursor="hand2",
    pady=3,
    command=show_hint
    )

btn_verify.pack(pady=6)
btn_hint.pack(pady=4)    

# Center the window on the screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":    
    # 5. START THE GAME
    load_images()
    window.mainloop()