import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from transcription_tool.transcriber import transcribe_audio
from transcription_tool.file_utils import save_transcription
import threading


def main():
    root = tk.Tk()
    root.title("Transcripción de Audio")
    root.geometry("500x500")

    language_var = tk.StringVar(value="es-ES")

    def select_file():
        audio_path = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.wav *.mp3")])
        if audio_path:
            progress_bar.start()
            transcription_thread = threading.Thread(
                target=transcribe_and_display,
                args=(audio_path,)
            )
            transcription_thread.start()

    def transcribe_and_display(audio_path):
        try:
            transcription = transcribe_audio(audio_path, language=language_var.get())
            if transcription:
                text_area.insert("1.0", transcription)
            else:
                messagebox.showerror("Error", "No se pudo transcribir el audio.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al transcribir: {e}")
        finally:
            progress_bar.stop()

    def save_file():
        content = text_area.get("1.0", tk.END)
        if content.strip():
            save_transcription(content)
        else:
            messagebox.showwarning("Advertencia", "No hay texto para guardar.")

    # Interfaz frame = tk.Frame(master=root, borderwidth=5)

    frame_1 = tk.Frame(master=root, relief=tk.RAISED, borderwidth=5)
    frame_1.pack(pady=10)
    tk.Label(frame_1, text="Selecciona el idioma:",
             foreground="white",  # Set the text color to white
             background="#34A2FE"  # Set the background color to black
             ).pack(pady=5)
    tk.OptionMenu(frame_1, language_var, "es-ES", "en-US", "pt-BR", "fr-FR").pack(pady=5)

    select_button = tk.Button(frame_1, text="Seleccionar Audio", command=select_file,
             foreground="white",  # Set the text color to white
             background="green")
    save_button = tk.Button(frame_1, text="Guardar Transcripción", command=save_file,
             foreground="white",  # Set the text color to white
             background="blue")

    frame_2 = tk.Frame(master=root, relief=tk.GROOVE, borderwidth=1)
    frame_2.pack(pady=10)
    progress_bar = ttk.Progressbar(frame_2, length=400, mode='indeterminate')

    frame_3 = tk.Frame(master=root, relief=tk.SUNKEN, borderwidth=1)
    frame_3.pack()
    text_area = tk.Text(frame_3, wrap=tk.WORD)

    select_button.pack(pady=10)
    save_button.pack(pady=10)
    progress_bar.pack(pady=10, fill=tk.X, padx=10)
    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    root.mainloop()
