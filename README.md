# 🎮💕 Valentine's Day Catching Game

<div align="center">

**A whimsical Valentine's Day digital card with a catching game!**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Kivy](https://img.shields.io/badge/Kivy-2.3.0%2B-brightgreen.svg)](https://kivy.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)]()

[Report Bug](https://github.com/joker24jq-ui/valentine-catching-game/issues) • [Request Feature](https://github.com/joker24jq-ui/valentine-catching-game/issues)

</div>

---

## 🌹 About The Game

A simple, charming Valentine's Day digital card with an interactive catching game. Ask the question, play the game, and share a customizable reward!

**Key Features:**
- Romantic question screen with evasive "No" button
- Catching game with adorable critters
- Customizable reward ticket system
- Whimsical music and sound effects

---

## 🎬 How It Works

### Screen 1: The Valentine Question
- "Will you be my valentine?" with two buttons
- The "No" button runs away from your cursor!
- Click "Yes" to start the game

### Screen 2: Catching Game
- Control a character with your mouse
- Catch 10 good critters to win
- Avoid bad items (they cost lives!)
- Start with 3 lives

### Screen 3: Win/Lose
- Game Over screen with retry option
- Victory screen with customizable reward tickets
- Save tickets as PNG images

---

## 🚀 Quick Start

### Run from Source

```bash
# Clone the repository
git clone https://github.com/joker24jq-ui/valentine-catching-game.git
cd valentine-catching-game

# Install dependencies
pip install -r requirements.txt

# Run the game
python valentine_game.py
```

### Build Your Own .exe

See [BUILD_GUIDE.md](BUILD_GUIDE.md) for complete instructions.

```bash
pip install pyinstaller
python -m PyInstaller valentine_game.spec --clean
```

---

## 🎨 Customization

Replace `assets/reward_ticket.png` with your own 800x400px image - perfect for personalizing your Valentine's card!

Full customization guide: [CUSTOMIZATION.md](CUSTOMIZATION.md)

---

## 🎮 Controls

| Input | Action |
|-------|--------|
| **Mouse Movement** | Move player left/right |
| **Arrow Keys** | Alternative movement |
| **Left Click** | Select buttons |

---

## 📂 Project Structure

```
valentine-catching-game/
├── valentine_game.py          # Main game code
├── valentine_game.spec         # Build configuration
├── requirements.txt            # Dependencies
├── cupid_ico.ico              # Game icon
├── fonts/Gothess.ttf          # Custom font
├── assets/                    # Images (backgrounds, sprites, reward)
├── music/                     # Background music
└── sounds/                    # Sound effects
```

---

## 🛠️ Technical Details

- **Python 3.8+** with **Kivy Framework**
- **Window Size:** 1000x700px
- **Custom Font:** Gothess
- **Audio:** MP3 background music and sound effects
- **Packaging:** PyInstaller for standalone .exe

---

## 🐛 Troubleshooting

- **Icon not showing:** Windows caches icons - try renaming the .exe
- **Audio delay:** Normal on first launch
- **Build errors:** See [BUILD_GUIDE.md](BUILD_GUIDE.md)

---

## 🤝 Contributing

Contributions welcome! Ideas:
- Difficulty levels
- High score system
- More critter types
- Mobile port
- Multiplayer mode

How to contribute:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📜 License

MIT License. See [LICENSE](LICENSE) file.

**Asset Attribution:**
- Images: AI-generated
- Sounds: Created from copyright-free sources
- Music: Copyright-free sources

---

## 👤 Author

**JDuke**

GitHub: [@joker24jq-ui](https://github.com/joker24jq-ui)

---

<div align="center">

**Made with 💕 for Valentine's Day 2026**

⭐ Star this repo if you enjoyed it!

</div>
