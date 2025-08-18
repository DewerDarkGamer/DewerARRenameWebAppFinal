#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main entry point for the Barcode Reader application
จุดเริ่มต้นหลักสำหรับแอพพลิเคชันอ่าน Barcode
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Check command line arguments to determine which app to run
    if len(sys.argv) > 1:
        if sys.argv[1] == "--desktop" or sys.argv[1] == "-d":
            # Run desktop application
            print("Starting Desktop Barcode Reader...")
            from barcode_desktop import main
            main()
        elif sys.argv[1] == "--web" or sys.argv[1] == "-w":
            # Run web application
            print("Starting Web Barcode Reader...")
            from app import app
            app.run(host='0.0.0.0', port=5000, debug=True)
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("Barcode Reader Application")
            print("Usage:")
            print("  python main.py --desktop  # Run desktop GUI application")
            print("  python main.py --web      # Run web application")
            print("  python main.py --help     # Show this help message")
        else:
            print(f"Unknown argument: {sys.argv[1]}")
            print("Use --help for usage information")
    else:
        # Default: run desktop application
        print("Starting Desktop Barcode Reader (default)...")
        from barcode_desktop import main
        main()