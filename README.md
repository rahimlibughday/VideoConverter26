# VideoConverter26

A lightweight desktop app for compressing video files, built with **Python**, **FFmpeg**, and a custom **CustomTkinter** interface inspired by Opera GX's dark, gradient-driven aesthetic.

## Features

- 🎥 **Any input video** — pick any video file, any size, any format supported by FFmpeg
- 💾 **Custom output** — choose your own destination folder and file name for the converted result
- ⚡ **Fast compression** — powered by FFmpeg's `libx264` encoder, with optional GPU-accelerated encoding for faster processing
- 🎨 **Opera GX–style UI** — dark theme with gradient accents, built entirely with CustomTkinter
- 📦 **Standalone build** — packaged as a single executable with PyInstaller, no separate Python or FFmpeg install required for end users

## How It Works

1. Launch the app.
2. Select the video you want to compress.
3. Choose where to save the output file and give it a name.
4. Hit convert — FFmpeg handles the encoding in the background while the UI stays responsive.

## Tech Stack

| Component | Purpose |
|---|---|
| Python | Core application logic |
| FFmpeg | Video encoding/compression engine |
| CustomTkinter | Modern, themeable GUI |
| PyInstaller | Bundling into a single executable |

## Installation (from source)

```bash
git clone https://github.com/rahimlibughday/VideoConverter26.git
cd VideoConverter26
pip install -r requirements.txt
python converter.py
```

> **Note:** FFmpeg must be available either on your system `PATH` or bundled alongside the app in the same directory as the executable.

## Building the Executable

```bash
pyinstaller --windowed --onefile --add-binary "ffmpeg:." converter.py
```

The finished executable will be in the `dist/` folder, with FFmpeg bundled inside — no console window, no extra setup for the end user.

## Roadmap

- [ ] Progress bar reflecting real-time FFmpeg encoding progress
- [ ] Batch conversion (multiple files at once)
- [ ] Preset quality profiles (e.g. "Small", "Balanced", "High Quality")
- [ ] Drag-and-drop file support

## License

This project is open source. Feel free to fork, modify, and contribute.
