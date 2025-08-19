
# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

block_cipher = None

a = Analysis(
    ['barcode_desktop_final.py'],
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
        'PIL.Image'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'pyzbar',
        'pyzbar.pyzbar',
        'pyzbar.wrapper',
        'pyzbar.zbar_library',
        'zbar',
        'libzbar',
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

# Remove any pyzbar related modules from pure python modules
if hasattr(a, 'pure'):
    a.pure = [x for x in a.pure if not any(
        pyzbar_module in str(x) for pyzbar_module in [
            'pyzbar', 'zbar', 'libzbar'
        ]
    )]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BarcodeReader_Final',
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
