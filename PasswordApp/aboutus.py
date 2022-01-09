import tkinter as tk

root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=30, width=65)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """This application aims to read all wifi passwords and visualizes the 
complexity in graph formation by taking into account several criteria and help you generate new random passwords."""
T.insert(tk.END, quote)
tk.mainloop()
