from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.title("Language Translator")
root.config(bg='ghost white')

Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='white smoke').pack()

Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=200, y=60)
Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)

Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=60)
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

language_codes = {name: code for code, name in LANGUAGES.items()}

language_names = list(language_codes.keys())

src_lang = ttk.Combobox(root, values=language_names, width=22)
src_lang.place(x=20, y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values=language_names, width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('choose output language')



def Translate():
    translator = Translator()
    src_code = language_codes.get(src_lang.get())
    dest_code = language_codes.get(dest_lang.get())

    if src_code and dest_code:
        try:
            translated = translator.translate(text=Input_text.get(1.0, END), src=src_code, dest=dest_code)
            Output_text.delete(1.0, END)
            Output_text.insert(END, translated.text)
        except Exception as e:
            Output_text.delete(1.0, END)
            Output_text.insert(END, f"Error: {str(e)}")
    else:
        Output_text.delete(1.0, END)
        Output_text.insert(END, "Error: Invalid language selection")


trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='royal blue1',
                   activebackground='sky blue')
trans_btn.place(x=490, y=180)

root.mainloop()
