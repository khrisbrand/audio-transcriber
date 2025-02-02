from tkinter import filedialog, messagebox

def save_transcription(content):
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if save_path:
        try:
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(content)
                messagebox.showinfo("Éxito", "Transcripción guardada con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
