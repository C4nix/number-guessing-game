
# 🎲 Number Guessing Game 🎯  

A fun and interactive number guessing game where you have to guess a randomly chosen number within a limited number of attempts.  
Different difficulty levels make the game more exciting! 🚀  

---

## 🔥 Features  
✅ **5 difficulty levels** (from "Very Easy" to "Very Hard")  
✅ **Limited attempts** based on difficulty level  
✅ **Hint system**: Tells you if your guess is too high or too low  
✅ **Easter Egg 🎁**: Guessing **23** gives you **one extra chance** (but only once!)  
✅ **Error handling**: Prevents crashes from invalid inputs  

---

## 📜 Difficulty Levels  
| Level       | Range       | Attempts Allowed |
|------------|------------|----------------|
| 1️⃣ Very Easy  | 1 - 10     | 10             |
| 2️⃣ Easy      | 1 - 30     | 8              |
| 3️⃣ Normal    | 1 - 50     | 8              |
| 4️⃣ Hard      | 1 - 100    | 7              |
| 5️⃣ Very Hard | 1 - 500    | 5              |

---

## 🎮 How to Play  
1️⃣ Run the script using Python:  
   ```bash
   python number_guessing.py
  ```
2️⃣ Choose a difficulty level (1-5).  
3️⃣ Enter your guesses and follow the hints!  
4️⃣ Find the correct number before you run out of attempts.  
5️⃣ Enjoy and try again to improve your guessing skills! 😎🔥  

---

## 🛠 Installation & Requirements  
🔹 Requires **Python 3.x**  
🔹 No external libraries needed (uses built-in Python modules)  

To clone the repository and start playing, run:  
```bash
git clone https://github.com/C4nix/number-guessing-game.git
cd number-guessing-game
python number_guessing.py
```

---

### 🎮 **Game Start:**  
```plaintext
🎲 Welcome to the Number Guessing Game! 🎯
**** Difficulty Levels ****
1. Very Easy (1-10)
2. Easy (1-30)
3. Normal (1-50)
4. Hard (1-100)
5. Very Hard (1-500)
********************************
Please choose a game level (1-5): 3
🔢 A number between 1 and 50 has been chosen. Try to guess it!
```

### 🤔 **User Guessing:**  
```plaintext
Enter your guess: 25
❌ Incorrect guess. ⬆️ Try a higher number!
You have 7 attempts left.
```

### 🎉 **Winning Message:**  
```plaintext
🎉 Congratulations! You found the number 42 in 5 attempts! 🎯
```

### 💀 **Game Over Message:**  
```plaintext
💀 Game Over! The correct number was 42. Better luck next time! 🎲
```

---

## 🚀 Future Enhancements  
- 🔹 **GUI version** using `Tkinter`  
- 🔹 **Leaderboard & best score tracking**  
- 🔹 **Custom difficulty range selection**  

---

## 🤝 Contributing  
Want to improve the game? Feel free to **fork** the repository, make changes, and submit a **pull request**!  

---

## ⚖️ License  
This project is licensed under the **MIT License**.  




