# App Icon Generation Guide

## 🎨 Custom App Icon: Person Reading a Book

This guide will help you generate the custom launcher icon for the Flutter Books API Workshop app.

## 📋 Prerequisites

1. **SVG to PNG Converter**: Use any online converter like:
   - [Convertio](https://convertio.co/svg-png/)
   - [CloudConvert](https://cloudconvert.com/svg-to-png)
   - [SVG to PNG](https://svgtopng.com/)

## 🔧 Steps to Generate Icon

### Step 1: Convert SVG to PNG
1. Open the file: `assets/icons/app_icon.svg`
2. Upload to your chosen SVG to PNG converter
3. Set output size to **1024x1024 pixels**
4. Download the PNG file

### Step 2: Save the Icon
1. Save the downloaded PNG as: `assets/icons/app_icon.png`
2. Ensure the file is exactly 1024x1024 pixels

### Step 3: Generate Platform Icons
```bash
# Install dependencies (if not already done)
flutter pub get

# Generate launcher icons for all platforms
flutter pub run flutter_launcher_icons:main
```

## 🎯 Icon Design Features

- **Person Reading**: Simple figure with reading glasses
- **Open Book**: With visible text lines and pages
- **Thought Bubble**: Indicating reading/thinking process
- **App Colors**: Matches the app theme (#F5E6D3, #8B4513)
- **Modern Style**: Clean, flat design that scales well

## 📱 Platform Support

The generated icon will work on:
- ✅ Android (various densities)
- ✅ iOS (iPhone & iPad)
- ✅ Web (PWA support)
- ✅ Windows
- ✅ macOS

## 🔄 Customization

To customize the icon:
1. Edit `assets/icons/app_icon.svg` or replace `assets/icons/app_icon.png`
2. Update colors in `pubspec.yaml` flutter_launcher_icons section
3. Re-run `flutter pub run flutter_launcher_icons:main`

## 🚀 Result

After following these steps, your app will have a beautiful custom launcher icon featuring a person reading a book, perfectly representing the Books API Workshop app! 