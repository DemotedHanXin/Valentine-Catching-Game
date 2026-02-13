# 🎨 Customization Guide

This guide shows you how to customize the Valentine's Day Catching Game with your own assets.

---

## 🎫 Replacing the Reward Ticket Image

The game includes a placeholder reward ticket. Here's how to add your own:

### Requirements
- **Image size:** 800x400 pixels (exactly)
- **Format:** PNG (supports transparency)
- **File name:** `reward_ticket.png`
- **Location:** `assets/reward_ticket.png`

### Steps
1. Create your reward image at 800x400px
2. Save as `reward_ticket.png`
3. Replace the file in `assets/reward_ticket.png`
4. Run the game - your custom image appears on the win screen!

**No code changes needed!**

---

## 🎨 Customizing Other Assets

### Backgrounds

**Valentine Question Screen**
- File: `assets/valentine_bg.png`
- Size: 1000x700px

**Gameplay Screen**
- File: `assets/level_bg.png`
- Size: 1000x700px

### Characters

**Player Sprite**
- File: `assets/girl.png`
- Size: 120x140px
- Use PNG with transparency

**Good Critters** (80x80px each)
- `assets/critter1.png`
- `assets/critter2.png`
- `assets/critter3.png`
- `assets/critter4.png`
- `assets/critter5.png`

**Bad Items** (80x80px each)
- `assets/badteddy.png`
- `assets/thornyrose.png`
- `assets/wiltedflower.png`

---

## 🎵 Audio Files

### Music (MP3 format, loops automatically)
- `music/1st screen whimsical.mp3` - Question screen
- `music/1st level strange.mp3` - Gameplay

### Sound Effects (MP3 format)
- `sounds/good_catch.mp3` - Catching good critter
- `sounds/bad_catch.mp3` - Catching bad item
- `sounds/sad_squeak.mp3` - Missing good critter
- `sounds/game_over.mp3` - Lose screen
- `sounds/reward_sound.mp3` - Win screen

**Simply replace the files** - keep the same filenames!

---

## 🎯 Icon

**Game Icon**
- File: `cupid_ico.ico` (root folder)
- Format: .ico (Windows icon format)
- Use online converter to create from PNG

---

## 🎭 Changing the Font

The game uses **Gothess** font (`fonts/Gothess.ttf`) for all text.

**To change:**
1. Replace `fonts/Gothess.ttf` with your font file
2. Keep filename as `Gothess.ttf`
3. OR edit `valentine_game.py` line 25 to point to new font name

---

## 💡 Tips

- **Keep backups** of original assets
- **Test after each change** to verify assets load
- **Image dimensions matter** - wrong sizes may cause issues
- **PNG format recommended** for images (transparency support)
- **MP3 format required** for audio files

---

## 🔧 After Customizing

### If running from source:
```bash
python valentine_game.py
```

### If building new .exe:
```bash
python -m PyInstaller valentine_game.spec --clean
```

Your customizations will be embedded in the new executable!

---

**Questions?** Open an issue on GitHub!
