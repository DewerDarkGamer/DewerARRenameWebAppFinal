#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyInstaller build script for Barcode Reader
สคริปต์สำหรับ build exe ของ Barcode Reader
"""

import os
import sys
from pathlib import Path

def build_exe():
    """Build EXE using PyInstaller"""
    try:
        import PyInstaller.__main__
        
        # Define build parameters
        script_name = "barcode_desktop.py"
        exe_name = "BarcodeReader"
        
        # PyInstaller arguments
        args = [
            script_name,
            f"--name={exe_name}",
            "--onefile",
            "--windowed",
            "--clean",
            "--noconfirm",
            "--add-data=README.md;.",
            "--hidden-import=tkinter",
            "--hidden-import=tkinter.filedialog", 
            "--hidden-import=tkinter.messagebox",
            "--hidden-import=tkinter.ttk",
            "--hidden-import=tkinter.scrolledtext",
            "--hidden-import=cv2",
            "--hidden-import=numpy",
            "--hidden-import=PIL",
            "--hidden-import=PIL.Image",
            "--hidden-import=pyzbar",
            "--hidden-import=pyzbar.pyzbar",
            "--exclude-module=matplotlib",
            "--exclude-module=pytest",
            "--exclude-module=setuptools",
            "--exclude-module=distutils",
            "--exclude-module=email",
            "--exclude-module=html",
            "--exclude-module=http",
            "--exclude-module=urllib3",
            "--exclude-module=xml",
            "--exclude-module=unittest",
        ]
        
        print("Building EXE with PyInstaller...")
        print(f"Command: pyinstaller {' '.join(args)}")
        
        # Run PyInstaller
        PyInstaller.__main__.run(args)
        
        # Check if build was successful
        exe_path = Path("dist") / f"{exe_name}.exe"
        if exe_path.exists():
            print(f"✓ Build successful! EXE created at: {exe_path}")
            print(f"✓ File size: {exe_path.stat().st_size / (1024*1024):.1f} MB")
        else:
            print("✗ Build failed - EXE not found")
            return False
            
        return True
        
    except ImportError:
        print("Error: PyInstaller not installed")
        print("Install with: pip install pyinstaller")
        return False
    except Exception as e:
        print(f"Error during build: {str(e)}")
        return False

if __name__ == "__main__":
    success = build_exe()
    sys.exit(0 if success else 1)

# Legacy PyInstaller spec configuration (if needed)
try:
    from PyInstaller.utils.hooks import collect_data_files
    
    # Collect data files for OpenCV  
    opencv_data = collect_data_files('cv2')

a = Analysis(
    ['barcode_desktop.py'],
    pathex=[],
    binaries=[],
    datas=opencv_data + [
        ('README.md', '.'),
    ],
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
        'threading',
        'pathlib',
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
        'unittest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

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
    console=False,  # Hide console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)