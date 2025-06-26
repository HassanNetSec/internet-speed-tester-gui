import tkinter as tk
from core.speed_checker import get_speed

def run_gui():
    root = tk.Tk()
    root.title("🌐 Internet Speed Test")
    root.geometry("450x300")
    root.config(bg="#e9f2fb")

    # Fonts & Colors
    title_font = ("Segoe UI", 18, "bold")
    label_font = ("Segoe UI", 11)
    button_font = ("Segoe UI", 11, "bold")
    bg_color = "#e9f2fb"
    btn_color = "#007acc"
    result_color = "#2e7d32"
    error_color = "#d32f2f"

    def test_speed():
        status.config(text="Testing... Please wait", fg="#555")
        result.config(text="")
        root.update()
        try:
            down, up, ping = get_speed()
            status.config(text="✅ Test Complete", fg=result_color)
            result.config(
                text=f"↓ Download: {down} Mbps\n↑ Upload: {up} Mbps\n🏓 Ping: {ping} ms",
                fg=result_color
            )
        except Exception as e:
            status.config(text="❌ Test Failed", fg=error_color)
            result.config(text=f"Error: {e}", fg=error_color)

    # Title
    tk.Label(root, text="Internet Speed Test", font=title_font, bg=bg_color).pack(pady=15)

    # Status
    status = tk.Label(root, text="", font=label_font, bg=bg_color)
    status.pack(pady=5)

    # Result display
    result = tk.Label(root, text="", font=("Consolas", 12), bg=bg_color, justify="center")
    result.pack(pady=10)

    # Button
    tk.Button(
        root, text="🚀 Start Speed Test", command=test_speed,
        bg=btn_color, fg="white", font=button_font, padx=20, pady=5,
        activebackground="#005f99", bd=0, relief="ridge", cursor="hand2"
    ).pack(pady=10)

    root.mainloop()
