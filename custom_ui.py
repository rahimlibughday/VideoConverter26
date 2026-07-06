import subprocess
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk

from convert_video import convert_video


class VideoConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Opera GX Video Converter")
        self.geometry("920x560")
        self.minsize(860, 520)
        self.configure(fg_color="#06070b")

        self._build_background()
        self._build_ui()

    def _build_background(self):
        self.canvas = tk.Canvas(self, bg="#06070b", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_rectangle(0, 0, 2200, 2200, fill="#0a0d14", outline="")
        self.canvas.create_oval(-180, -160, 420, 320, fill="#1c0d16", outline="")
        self.canvas.create_oval(520, -90, 980, 360, fill="#140a10", outline="")
        self.canvas.create_rectangle(0, 350, 2200, 2200, fill="#08090f", outline="")

        self.canvas.create_line(110, 100, 700, 100, fill="#ff4d4d", width=2, dash=(4, 4))
        self.canvas.create_line(120, 430, 760, 430, fill="#ff4d4d", width=2, dash=(4, 4))

    def _build_ui(self):
        container = ctk.CTkFrame(
            self,
            fg_color="#10131b",
            corner_radius=24,
            border_width=1,
            border_color="#ff4d4d",
        )
        container.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

        header = ctk.CTkFrame(container, fg_color="transparent")
        header.pack(fill="x", padx=26, pady=(24, 10))

        title = ctk.CTkLabel(
            header,
            text="Video Converter",
            font=("Segoe UI", 24, "bold"),
            text_color="#ff4d4d",
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Pick a video, choose a folder, type the output name, and let the red glow handle the rest.",
            font=("Segoe UI", 12),
            text_color="#b6bccd",
            justify="left",
        )
        subtitle.pack(anchor="w", pady=(6, 0))

        form = ctk.CTkFrame(container, fg_color="#171a24", corner_radius=18)
        form.pack(fill="both", expand=True, padx=22, pady=(6, 12))

        self.input_var = tk.StringVar()
        self.output_dir_var = tk.StringVar()
        self.output_name_var = tk.StringVar(value="converted_video.mp4")

        self._build_field(form, "Input video", self.input_var, self._pick_input_path)
        self._build_field(form, "Output folder", self.output_dir_var, self._pick_output_folder)
        self._build_field(form, "Output name", self.output_name_var)

        buttons = ctk.CTkFrame(form, fg_color="transparent")
        buttons.pack(fill="x", padx=16, pady=(16, 8))

        convert_btn = ctk.CTkButton(
            buttons,
            text="Convert",
            command=self._convert,
            fg_color="#ff4d4d",
            hover_color="#ff2f2f",
            text_color="#ffffff",
            corner_radius=14,
            border_width=1,
            border_color="#ff6f6f",
            width=160,
            height=42,
        )
        convert_btn.pack(side="left")
        self._attach_hover_effect(convert_btn)

        clear_btn = ctk.CTkButton(
            buttons,
            text="Clear",
            command=self._clear_fields,
            fg_color="#1b1f2c",
            hover_color="#272d3b",
            text_color="#f3f4f6",
            corner_radius=14,
            border_width=1,
            border_color="#2c3344",
            width=120,
            height=42,
        )
        clear_btn.pack(side="left", padx=(12, 0))
        self._attach_hover_effect(clear_btn)

        self.status_label = ctk.CTkLabel(
            form,
            text="Ready to start converting.",
            font=("Segoe UI", 11),
            text_color="#9e9fb4",
            anchor="w",
        )
        self.status_label.pack(anchor="w", padx=16, pady=(8, 0))

    def _build_field(self, parent, label_text, var, browse_command=None):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=16, pady=10)

        ctk.CTkLabel(frame, text=label_text, font=("Segoe UI", 11, "bold"), text_color="#f3f4f6").pack(anchor="w", pady=(0, 6))

        entry_frame = ctk.CTkFrame(frame, fg_color="#1a1d28", corner_radius=14, border_width=1, border_color="#2a2f3f")
        entry_frame.pack(fill="x")

        entry = ctk.CTkEntry(
            entry_frame,
            textvariable=var,
            fg_color="#1a1d28",
            border_color="#2a2f3f",
            border_width=1,
            text_color="#fefefe",
            placeholder_text="",
            height=42,
        )
        entry.pack(side="left", fill="x", expand=True, padx=(10, 6), pady=8)

        if browse_command is not None:
            button = ctk.CTkButton(
                entry_frame,
                text="Browse",
                command=browse_command,
                width=90,
                height=34,
                fg_color="#2a2f3f",
                hover_color="#3b4257",
                text_color="#f3f4f6",
                corner_radius=10,
            )
            button.pack(side="right", padx=(0, 10), pady=8)
            self._attach_hover_effect(button)

    def _attach_hover_effect(self, widget):
        widget.bind("<Enter>", lambda event: self._animate_widget(widget, True))
        widget.bind("<Leave>", lambda event: self._animate_widget(widget, False))

    def _animate_widget(self, widget, hover):
        try:
            widget.configure(border_width=2 if hover else 1)
        except Exception:
            pass

    def _pick_input_path(self):
        path = filedialog.askopenfilename(
            title="Select input video",
            filetypes=[
                ("Video files", "*.mp4 *.mkv *.avi *.mov *.webm *.m4v"),
                ("All files", "*.*"),
            ],
        )
        if path:
            self.input_var.set(path)
            self.status_label.configure(text=f"Selected input: {Path(path).name}")

    def _pick_output_folder(self):
        folder = filedialog.askdirectory(title="Select output folder")
        if folder:
            self.output_dir_var.set(folder)
            self.status_label.configure(text=f"Selected folder: {Path(folder).name}")

    def _convert(self):
        input_path = self.input_var.get().strip()
        output_dir = self.output_dir_var.get().strip()
        output_name = self.output_name_var.get().strip()

        if not input_path:
            messagebox.showwarning("Missing input", "Please choose an input video file.")
            return

        if not output_dir:
            messagebox.showwarning("Missing folder", "Please choose a folder to save the converted file.")
            return

        if not output_name:
            messagebox.showwarning("Missing name", "Please enter a name for the output video.")
            return

        if "." not in output_name:
            output_name += ".mp4"

        output_path = str(Path(output_dir) / output_name)
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        self.status_label.configure(text="Converting video, please wait...")
        self.update_idletasks()

        try:
            convert_video(input_path, output_path)
            messagebox.showinfo("Conversion complete", f"Saved to:\n{output_path}")
            self.status_label.configure(text="Conversion completed successfully.")
        except FileNotFoundError as exc:
            messagebox.showerror("ffmpeg not found", str(exc))
            self.status_label.configure(text="ffmpeg is not available on PATH.")
        except subprocess.CalledProcessError as exc:
            messagebox.showerror("Conversion failed", f"ffmpeg exited with code {exc.returncode}.")
            self.status_label.configure(text="Conversion failed.")

    def _clear_fields(self):
        self.input_var.set("")
        self.output_dir_var.set("")
        self.output_name_var.set("converted_video.mp4")
        self.status_label.configure(text="Ready to start converting.")


def run_app():
    app = VideoConverterApp()
    app.mainloop()


if __name__ == "__main__":
    run_app()
