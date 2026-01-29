# Flashcard Game – French to English Vocabulary Trainer

This is a Tkinter-based flashcard application that helps users learn French vocabulary by flipping cards to reveal English meanings. The app tracks known words and stores progress locally so that learned words are not repeated.

---

## Features

- Displays a French word on a flashcard
- Automatically flips the card after 3 seconds to show the English meaning
- Allows users to mark words as **known** or **unknown**
- Removes known words from the learning list
- Saves progress in a CSV file so learning persists across sessions
- Uses a clean GUI with image-based flashcards and buttons

---

## Technologies Used

- Python
- Tkinter (GUI)
- Pandas (data handling)
- CSV files for data persistence

---

## How It Works

1. On startup, the app tries to load `words_to_learn.csv`
2. If the file does not exist, it loads `french_words.csv`
3. A random French word is displayed on the flashcard
4. After 3 seconds, the card flips to show the English translation
5. Clicking:
   - ❌ (wrong) shows the next card
   - ✔️ (right) removes the word from the list and saves progress
6. The app continues until all words are learned

---

## Learning Outcome

This project demonstrates:
- Event-driven GUI programming
- Timer-based state changes
- Persistent data storage
- Clean separation of UI and logic

---



