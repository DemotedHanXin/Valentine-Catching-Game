# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['valentine_game.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('fonts/Gothess.ttf', 'fonts'),
        ('assets/*.png', 'assets'),
        ('music/*.mp3', 'music'),
        ('sounds/*.mp3', 'sounds'),
    ],
    hiddenimports=[
        'kivy.core.window',
        'kivy.core.audio',
        'kivy.core.audio.audio_sdl2',
        'kivy.core.image',
        'kivy.core.text',
        'kivy.graphics',
        'kivy.graphics.texture',
        'kivy.uix.button',
        'kivy.uix.label',
        'kivy.uix.widget',
        'kivy.uix.screenmanager',
        'kivy.clock',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ValentineGame',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='cupid_ico.ico',

)