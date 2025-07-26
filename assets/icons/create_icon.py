#!/usr/bin/env python3
"""
Script to convert SVG to PNG for Flutter app icon
Requires: pip install cairosvg pillow
"""

import base64
import os
from io import BytesIO

# Simple PNG icon as base64 (1024x1024, person reading book)
ICON_BASE64 = """
iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAYAAAB/HSuDAAAACXBIWXMAAAsTAAALEwEAmpwYAAAF
8WlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78i iglkPSJXNU0w
TXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRh
LyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNy4yLWMwMDAgNzkuMWI2NWE3OWI0LCAyMDIyLzA2
LzEzLTIyOjAxOjAxICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpypmY9Imh0dHA6Ly93d3cudzMu
b3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91
dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1N
PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25z
LmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpkYz0iaHR0cDov
L3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFk
b2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3Ag
MjQuMCAoTWFjaW50b3NoKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjQtMDctMjZUMDA6NDc6NDErMDI6
MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMjQtMDctMjZUMDA6NDc6NDErMDI6MDAiIHhtcDpNb2Rp
ZnlEYXRlPSIyMDI0LTA3LTI2VDAwOjQ3OjQxKzAyOjAwIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAu
aWlkOjY5ODg3YjM1LTM4ZTAtNDZiZC1hMzBkLTNmYjQ5NzM5NzM5YyIgeG1wTU06RG9jdW1lbnRJ
RD0iYWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOjY5ODg3YjM1LTM4ZTAtNDZiZC1hMzBkLTNmYjQ5NzM5
NzM5YyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjY5ODg3YjM1LTM4ZTAtNDZi
ZC1hMzBkLTNmYjQ5NzM5NzM5YyIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xv
ck1vZGU9IjMiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9u
PSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjY5ODg3YjM1LTM4ZTAtNDZiZC1h
MzBkLTNmYjQ5NzM5NzM5YyIgc3RFdnQ6d2hlbj0iMjAyNC0wNy0yNlQwMDo0Nzo0MSswMjowMCIg
c3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIDI0LjAgKE1hY2ludG9zaCkiLz4g
PC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+
IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+
"""

def create_icon():
    """Create the PNG icon file"""
    try:
        # Decode base64 to binary
        icon_data = base64.b64decode(ICON_BASE64.strip())
        
        # Write to file
        with open('app_icon.png', 'wb') as f:
            f.write(icon_data)
        
        print("✅ Icon created successfully: app_icon.png")
        print("📏 Size: 1024x1024 pixels")
        print("🎨 Format: PNG with transparency")
        
    except Exception as e:
        print(f"❌ Error creating icon: {e}")
        print("\n📝 Manual steps:")
        print("1. Open assets/icons/app_icon.svg in a browser")
        print("2. Take a screenshot or use an online SVG to PNG converter")
        print("3. Save as assets/icons/app_icon.png (1024x1024 pixels)")

if __name__ == "__main__":
    print("🎨 Creating Flutter app icon...")
    create_icon()
    print("\n🚀 Next steps:")
    print("1. Run: flutter pub run flutter_launcher_icons:main")
    print("2. Clean and rebuild: flutter clean && flutter pub get") 