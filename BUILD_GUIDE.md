# 🛠️ Complete Build Guide - Creating the Standalone .exe

This guide will walk you through building your own Windows executable from source code.

---

## 📋 Prerequisites

### Required Software

**Python 3.8 or higher** (tested with Python 3.13.12)
- Download: https://www.python.org/downloads/
- ⚠️ **Important:** During installation, check "Add Python to PATH"

### Verify Installation

Open Command Prompt and run:
```bash
python --version
pip --version
```

Expected output:
```
Python 3.x.x
pip 24.x.x
```

---

## 🚀 Step-by-Step Build Instructions

### Step 1: Get the Source Code

Choose the method that applies to you:

#### Option A: Clone from GitHub (if using Git)

```bash
git clone https://github.com/joker24jq-ui/valentine-catching-game.git
cd valentine-catching-game
```

#### Option B: Download ZIP from GitHub

1. Go to the GitHub repository
2. Click the green "**Code**" button
3. Select "**Download ZIP**"
4. Extract the ZIP to a folder (e.g., `C:\Valentine`)
5. Open Command Prompt in that folder:
   - Navigate to the folder in File Explorer
   - Hold **Shift** + Right-click in empty space
   - Select "**Open PowerShell window here**" or "**Open command window here**"

#### Option C: Already Have the Files

If you already have all the game files (from a friend, USB drive, etc.):

1. Make sure you have ALL these files and folders:
   - `valentine_game.py` (main code file)
   - `valentine_game.spec` (build configuration)
   - `cupid_ico.ico` (icon file)
   - `fonts/` folder with `Gothess.ttf`
   - `assets/` folder with all PNG images
   - `music/` folder with MP3 files
   - `sounds/` folder with MP3 files

2. Open Command Prompt in the folder containing these files:
   - Navigate to the folder in File Explorer
   - Hold **Shift** + Right-click in empty space
   - Select "**Open PowerShell window here**" or "**Open command window here**"

**Verify you're in the right folder:**
```bash
dir
```

You should see `valentine_game.py` in the list.

---

### Step 2: Install Python Dependencies

```bash
pip install kivy pyinstaller
```

**This installs:**
- `kivy` - The game framework (graphics, audio, window management)
- `pyinstaller` - Tool to bundle Python + your code into a standalone .exe

**Troubleshooting:**
- If `pip` not recognized: Use `python -m pip install kivy pyinstaller`
- If permission errors: Add `--user` flag: `pip install --user kivy pyinstaller`
- If Kivy installation fails: Try `pip install kivy[base]`

**This may take 2-5 minutes** depending on your internet speed.

---

### Step 3: Test the Game from Source

Before building the .exe, verify everything works:

```bash
python valentine_game.py
```

**Expected behavior:**
- ✅ Window opens (1000x700 pixels)
- ✅ Valentine question screen appears with background
- ✅ Background music plays
- ✅ Both buttons are visible and clickable
- ✅ "No" button runs away when mouse approaches
- ✅ Clicking "Yes" transitions to gameplay
- ✅ All sprites and sounds work properly

**If something doesn't work:**

1. **Check folder structure:**
   ```
   Your_Folder/
   ├── valentine_game.py       ← Must be here
   ├── valentine_game.spec     ← Must be here
   ├── cupid_ico.ico          ← Must be here
   ├── fonts/                 ← Folder must exist
   │   └── Gothess.ttf
   ├── assets/                ← Folder must exist
   │   └── (all PNG files)
   ├── music/                 ← Folder must exist
   │   └── (all MP3 files)
   └── sounds/                ← Folder must exist
       └── (all MP3 files)
   ```

2. **Check console for error messages** - they'll tell you what's missing

3. **Verify file names match exactly** (case-sensitive on some systems)

---

### Step 4: Build the Standalone Executable

Once the game runs from source, you're ready to build!

```bash
python -m PyInstaller valentine_game.spec --clean
```

**What happens during build:**
1. PyInstaller reads the `.spec` configuration file
2. Bundles Python interpreter + Kivy framework + all dependencies
3. Embeds ALL your assets (images, sounds, music, fonts)
4. Creates a single standalone .exe with the custom Cupid icon
5. Takes 2-5 minutes depending on your system speed

**You'll see output like:**
```
INFO: PyInstaller: 6.x.x
INFO: Python: 3.x.x
INFO: Building EXE from EXE-00.toc
INFO: Building EXE from EXE-00.toc completed successfully.
```

**Build output structure:**
```
Your_Folder/
├── build/              ← Temporary files (can delete after)
├── dist/
│   └── ValentineGame.exe   ← YOUR FINISHED GAME! 🎉
└── (all your source files)
```

---

### Step 5: Test Your Executable

1. Open File Explorer
2. Navigate to the `dist/` folder inside your game folder
3. Find `ValentineGame.exe`
4. **Double-click to launch**

**The game should run without Python installed!**

### Complete Testing Checklist

Test thoroughly to ensure the build worked correctly:

**Screen 1 - Valentine Question:**
- [ ] Window opens at correct size
- [ ] Background image displays
- [ ] Question text is visible and readable
- [ ] Both buttons appear and are clickable
- [ ] "No" button runs away from cursor
- [ ] Background music plays
- [ ] Clicking "Yes" transitions to gameplay

**Screen 2 - Gameplay:**
- [ ] Gameplay background loads
- [ ] Music transitions smoothly
- [ ] Player sprite follows mouse
- [ ] Score displays (0/10)
- [ ] Lives display (3)
- [ ] Critters spawn and fall
- [ ] Collision detection works
- [ ] Sound effects play (catch, miss)
- [ ] Game ends at 10/10 (win) or 0 lives (lose)

**Screen 3 - Results:**
- [ ] Win screen appears with reward ticket
- [ ] Lose screen appears with retry button
- [ ] "Save Tickets" opens file dialog
- [ ] Can save reward as PNG file
- [ ] "Play Again" restarts game

**Other:**
- [ ] Custom Cupid icon shows in taskbar
- [ ] No console window appears
- [ ] .exe is 150-250MB (typical size)

---

## 🎨 Building with Custom Assets

Want to customize the game before building your .exe?

### You Can Replace:

1. **Reward Ticket:** `assets/reward_ticket.png` (800x400px)
2. **Backgrounds:** `assets/valentine_bg.png` or `level_bg.png` (1000x700px)
3. **Critters:** `assets/critter1.png` through `critter5.png` (80x80px)
4. **Player:** `assets/girl.png` (120x140px)
5. **Music:** Any MP3 files in `music/` folder
6. **Sounds:** Any MP3 files in `sounds/` folder

See [CUSTOMIZATION.md](CUSTOMIZATION.md) for detailed instructions and exact dimensions.

**After customizing, rebuild:**
```bash
python -m PyInstaller valentine_game.spec --clean
```

Your custom assets will be embedded in the new .exe!

---

## 📦 Understanding the Build Files

### valentine_game.spec

This is the PyInstaller configuration file that controls how your .exe is built.

**Key sections explained:**

```python
datas=[
    ('fonts/Gothess.ttf', 'fonts'),     # Bundles the custom font
    ('assets/*.png', 'assets'),          # Bundles all PNG images
    ('music/*.mp3', 'music'),            # Bundles background music
    ('sounds/*.mp3', 'sounds'),          # Bundles sound effects
],
```

```python
icon='cupid_ico.ico',    # Sets the .exe icon (must be .ico format)
console=False,            # Hides console window (clean launch)
name='ValentineGame',     # Name of output .exe file
```

### Want to Modify the .spec File?

**Change the .exe name:**
```python
name='YourCustomName',  # In the EXE() section
```

**Change the icon:**
```python
icon='your_custom_icon.ico',  # Must be .ico format, not PNG
```

**Add more data files:**
```python
datas=[
    ('your_folder/*.*', 'your_folder'),
],
```

**After any .spec modifications, rebuild:**
```bash
python -m PyInstaller valentine_game.spec --clean
```

---

## 🐛 Troubleshooting

### "Python is not recognized as a command"

**Problem:** Python not added to system PATH during installation

**Solution Option 1 - Use full path:**
```bash
C:\Users\YourName\AppData\Local\Programs\Python\Python313\python.exe -m PyInstaller valentine_game.spec --clean
```

**Solution Option 2 - Reinstall Python:**
1. Uninstall Python
2. Download fresh installer from python.org
3. During install, CHECK "Add Python to PATH"
4. Install and try again

---

### "No module named 'kivy'" or "'pyinstaller'"

**Problem:** Dependencies not installed

**Solution:**
```bash
python -m pip install kivy pyinstaller
```

Make sure you're using the same Python environment where you'll build the .exe.

---

### Icon Doesn't Display on .exe

**Problem:** Windows icon cache needs refresh

**This is cosmetic only - the icon IS embedded (check build logs for confirmation)**

**Solutions to force refresh:**
1. **Rename the .exe:** `ValentineGame.exe` → `Valentine.exe`
2. **Clear icon cache:**
   - Open Command Prompt as Administrator
   - Run: `ie4uinit.exe -show`
   - Restart Windows Explorer
3. **Reboot Windows** (forces complete cache clear)

---

### Audio Doesn't Play in .exe

**Problem:** Audio files not bundled or codec issues

**Solutions:**
1. Verify audio files exist in folders BEFORE building
2. Test game from source first: `python valentine_game.py`
3. Check `.spec` file includes music/sounds:
   ```python
   datas=[
       ('music/*.mp3', 'music'),
       ('sounds/*.mp3', 'sounds'),
   ],
   ```
4. Some systems need codecs: [K-Lite Codec Pack](https://codecguide.com/download_kl.htm)
5. Rebuild with `--clean` flag

---

### Build Fails with "Permission Denied"

**Problem:** Files locked or insufficient permissions

**Solutions:**
1. Close ALL running instances of the game or .exe
2. Manually delete `build/` and `dist/` folders
3. Run Command Prompt as Administrator:
   - Search for "cmd" in Start Menu
   - Right-click Command Prompt
   - Select "Run as administrator"
4. Navigate to game folder and rebuild

---

### .exe is Huge (Over 500MB)

**Problem:** PyInstaller bundles complete Python environment

**This is normal!** The .exe includes:
- Full Python interpreter (~50MB)
- Complete Kivy framework (~100MB)
- All Python dependencies
- Your game assets

**Typical size: 150-250MB** depending on asset sizes

**This CANNOT be significantly reduced** without breaking functionality.

---

### Game Works from Source but .exe Crashes

**Problem:** Assets not properly bundled or path issues

**Solutions:**
1. Verify `.spec` file `datas=` section includes ALL folders
2. Check `resource_path()` function is used in code (already implemented)
3. Build with `--clean` flag: `python -m PyInstaller valentine_game.spec --clean`
4. Temporarily change `console=False` to `console=True` in `.spec` to see error messages
5. Rebuild and check console for specific errors

---

### "Failed to execute script valentine_game"

**Problem:** Missing dependency or asset

**Solution:**
1. Build with console visible (change `.spec` file: `console=True`)
2. Rebuild: `python -m PyInstaller valentine_game.spec --clean`
3. Run the .exe - console will show exact error
4. Fix the issue (usually missing file or wrong path)
5. Change back to `console=False` and rebuild

---

## 📊 Build Performance & Requirements

**Typical build times:**
- First build: 3-5 minutes
- Subsequent builds: 2-3 minutes
- With `--clean` flag: 3-5 minutes (recommended)

**System requirements for building:**
- Windows 7 or higher
- 2GB free RAM during build
- 500MB free disk space
- Python 3.8+ installed

**Final .exe requirements to RUN:**
- Windows 7 or higher
- 50MB free disk space
- Audio output device (for music/sounds)
- **No Python installation needed!**

---

## ✅ Pre-Distribution Checklist

Before sharing your .exe with others:

**Build Quality:**
- [ ] Game runs completely from source without errors
- [ ] All assets customized as desired (especially reward ticket!)
- [ ] PyInstaller build completes without errors or warnings
- [ ] .exe launches without Python installed

**Functionality:**
- [ ] All three screens work correctly
- [ ] All sounds and music play properly
- [ ] Button interactions work (especially the evasive "No" button!)
- [ ] Collision detection accurate
- [ ] File save dialog works for reward tickets
- [ ] No console window appears

**Distribution:**
- [ ] Tested on a different computer (if possible)
- [ ] File size reasonable (150-250MB typical)
- [ ] Custom icon displays correctly
- [ ] Included instructions for players

---

## 🎉 Success!

**Congratulations! You've built a standalone game executable!**

Your `ValentineGame.exe` is now:
- ✅ **Self-contained** - No Python needed to run
- ✅ **Portable** - Copy to any Windows PC
- ✅ **Single file** - All assets embedded
- ✅ **Professional** - Custom icon, no console

---

## 📤 What's Next?

### Share Your Creation
- Send to friends, family, significant other
- Create a GitHub Release for others to download
- Upload to itch.io or other game platforms
- Post on social media (Reddit, Twitter, etc.)

### Customize Further
- Replace reward ticket with personal message
- Add your own backgrounds and music
- Modify gameplay (see source code)
- Create themed versions (birthdays, holidays)

### Keep Learning
- Study the Python/Kivy source code
- Experiment with game mechanics
- Build more projects!

---

**Questions or issues?** Open an issue on the [GitHub repository](https://github.com/joker24jq-ui/valentine-catching-game/issues)!

**Happy building!** 🎮💕✨
