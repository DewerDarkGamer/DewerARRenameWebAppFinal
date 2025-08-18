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
            "--hidden-import=pyzbar.wrapper",
            "--hidden-import=pyzbar.zbar_library",
            "--collect-all=pyzbar",
            "--collect-binaries=pyzbar",
            "--collect-data=pyzbar",
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
        
        # Check if custom spec file exists
        spec_file = "BarcodeReader.spec"
        if os.path.exists(spec_file):
            print(f"Using custom spec file: {spec_file}")
            PyInstaller.__main__.run([spec_file])
        else:
            print("Using command line arguments")
            # Run PyInstaller
            PyInstaller.__main__.run(args)
        
        # Check if build was successful
        exe_path = Path("dist") / f"{exe_name}.exe"
        if exe_path.exists():
            print(f"[SUCCESS] Build successful! EXE created at: {exe_path}")
            print(f"[INFO] File size: {exe_path.stat().st_size / (1024*1024):.1f} MB")
        else:
            print("[ERROR] Build failed - EXE not found")
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
