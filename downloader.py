import tkinter as tk
from tkinter import ttk
import os
import random



def selected_type(tipus):
    if tipus != None:
        master = tk.Tk()
        master.geometry("200x150")

        if tipus == "Videó":
            master.title("Videó letöltő")
            tk.Label(master, text="Videó letöltő", bg="lightgray", fg="black", font= ('Aerial 17 bold italic')).grid(row=0, column=1)
        elif tipus == "Zene":
            master.title("Zene letöltő")
            tk.Label(master, text="Zene letöltő", bg="lightgray", fg="black", font= ('Aerial 17 bold italic')).grid(row=0, column=1)


        tk.Label(master, text='Link:', font= ('Aerial 13')).grid(row=1)
        e1 = tk.Entry(master)
        e1.grid(row=1, column=1)


        def down():
            link = e1.get().strip()
            if tipus != None and link != None and link != "" and link != " ":
                os.system('echo Letöltés...')

                directory = os.getcwd()
                newdict = random.randint(1, 1000)
                exists = os.path.exists(directory + '/' + ("down_" + str(newdict)))
                
                while exists:
                    newdict = random.randint(1, 1000)
                    exists = os.path.exists(directory + '/' + ("down_" + str(newdict)))
                    if not exists:
                        break

                try:
                    os.mkdir(("down_" + str(newdict)))
                    print(f"A(z) '{("down_" + str(newdict))}' mappa sikeresen létrehozva!.")
                except FileExistsError:
                    print(f"A(z) '{("down_" + str(newdict))}' mappa már létezik.")
                except Exception as e:
                    print(f"Hiba: {e}")

                if tipus == "Videó":
                    os.system(f'yt-dlp -f "bestvideo+bestaudio[ext=m4a]" --merge-output-format mp4 --write-sub --embed-subs -o "{directory}/{"down_" + str(newdict)}/%(title)s.%(ext)s" {link}')
                    #os.system(f'yt-dlp -f bestvideo+bestaudio -o "{directory}/{"down_" + str(newdict)}/%(title)s.%(ext)s" {link}')
                elif tipus == "Zene":
                    os.system(f'yt-dlp -x --audio-format mp3 -o "{directory}/{"down_" + str(newdict)}/%(title)s.%(ext)s" {link}')




        button1 = ttk.Button(master, text='Mehet!', command=down).grid(row=2, column=1)
        button2 = tk.Button(master, text='Bezárás', width=10, command=master.destroy).grid(row=3, column=1)
        master.mainloop()



def on_select(event):
    selected_item = combo_box.get()
    label.config(text="Típus: " + selected_item)

    selected_type(selected_item)



root = tk.Tk()
root.title("Youtube letöltő")
root.geometry("200x140")

label = tk.Label(root, text="Típus: ")
label.pack(pady=10)

combo_box = ttk.Combobox(root, values=["Videó", "Zene"])
combo_box.pack(pady=5)

combo_box.set("Videó")

combo_box.bind("<<ComboboxSelected>>", on_select)


button = tk.Button(root, text='Bezárás', width=10, command=root.destroy)
button.pack()


root.mainloop()