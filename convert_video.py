import shutil
import subprocess
import sys
from pathlib import Path


def _find_ffmpeg() -> str:
    candidates = []

    if getattr(sys, "frozen", False):
        base_dir = Path(sys.executable).resolve().parent
        candidates.extend([base_dir / "ffmpeg", base_dir / "ffmpeg.exe"])
        if hasattr(sys, "_MEIPASS"):
            meipass_dir = Path(sys._MEIPASS).resolve()
            candidates.extend([meipass_dir / "ffmpeg", meipass_dir / "ffmpeg.exe"])
    else:
        base_dir = Path(__file__).resolve().parent
        candidates.extend([base_dir / "ffmpeg", base_dir / "ffmpeg.exe"])

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return str(candidate)

    for name in ("ffmpeg", "ffmpeg.exe"):
        found = shutil.which(name)
        if found:
            return found

    raise FileNotFoundError("ffmpeg was not found in the current folder, PATH, or bundled executable")


def convert_video(input_file: str, output_file: str) -> None:
    """Convert a video to H.264/AAC using ffmpeg."""
    ffmpeg_path = _find_ffmpeg()

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        ffmpeg_path,
        "-i",
        input_file,
        "-vcodec",
        "libx264",
        "-crf",
        "28",
        "-preset",
        "medium",
        "-acodec",
        "aac",
        "-b:a",
        "128k",
        str(output_path),
    ]

    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 convert_video.py <input_video> <output_video>")
        raise SystemExit(1)

    convert_video(sys.argv[1], sys.argv[2])
    print("Conversion completed successfully.")


def convert_video(input_file: str, output_file: str) -> None:
    """Convert a video to H.264/AAC using ffmpeg."""
    ffmpeg_path = shutil.which("ffmpeg")
    if not ffmpeg_path:
        raise FileNotFoundError("ffmpeg was not found in your PATH")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        ffmpeg_path,
        "-i",
        input_file,
        "-vcodec",
        "libx264",
        "-crf",
        "28",
        "-preset",
        "medium",
        "-acodec",
        "aac",
        "-b:a",
        "128k",
        str(output_path),
    ]

    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 convert_video.py <input_video> <output_video>")
        raise SystemExit(1)

    convert_video(sys.argv[1], sys.argv[2])
    print("Conversion completed successfully.")
