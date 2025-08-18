
# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

block_cipher = None

a = Analysis(
    ['barcode_desktop.py'],
    pathex=[],
    binaries=[],
    datas=[('README.md', '.')],
    hiddenimports=[
        'tkinter',
        'tkinter.filedialog',
        'tkinter.messagebox', 
        'tkinter.ttk',
        'tkinter.scrolledtext',
        'cv2',
        'numpy',
        'PIL',
        'PIL.Image',
        'pyzbar',
        'pyzbar.pyzbar',
        'pyzbar.wrapper',
        'pyzbar.zbar_library'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'pytest', 
        'setuptools',
        'distutils',
        'email',
        'html',
        'http',
        'urllib3',
        'xml',
        'unittest'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Collect all pyzbar data and binaries
from PyInstaller.utils.hooks import collect_all
datas, binaries, hiddenimports = collect_all('pyzbar')
a.datas += datas
a.binaries += binaries
a.hiddenimports += hiddenimports

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BarcodeReader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
