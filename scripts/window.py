# INTEL WRITER // NOTES ;;

# NEXT TASK: IMPORT A DIRECT LINK TO EACH ARTICLE/SEARCH TERM, REDIRECT TO THE NEAREST PAGE
# add highlight row feature
# organize output structures / filter web scraping results / string..
# consolidate new features into (wiki search option // google first blog options.. )

from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from scripts import scraper

# --INIT WINDOW--

window = Tk()
window.title('IntelWriter')
window.resizable(0, 0)
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth() / 2.5 - windowWidth)
positionDown = int(window.winfo_screenheight() / 3 - windowHeight)
window.geometry("600x600+{}+{}".format(positionRight, positionDown))

# menu

menubar = Menu(window)
window.config(menu=menubar)

# widgets

def empty_row(frame, quantity):
    for _ in range(quantity):
        empty = Label(frame, text=" ", font="none 12", anchor=CENTER).pack()



def submit_click():
    while True:
        entered_text = subject_entry.get()

        if entered_text == "":
            print("not accepted")
            break

        if entered_text != "":
            edit_window(scraper.search_subject(entered_text))
            break

# search display
search_frame = Frame(window)
empty_row(window, 1)
title_label = Label(search_frame, text="INTEL WRITER",
                    font="times 12 bold", anchor=CENTER).pack()
empty_row(search_frame, 1)
enter_label = Label(search_frame, text="Enter subject:",
                    font="times 12", anchor=CENTER)
enter_label.pack()
subject_entry = Entry(search_frame)
subject_entry.pack()
empty_row(search_frame, 1)
submit_button = Button(search_frame, text="submit", font="times 12",
                       height=1, width=6, command=submit_click)
submit_button.pack(side=TOP)
search_frame.pack()

def hello():
    messagebox.showinfo("hello")

def new_file():
    edit_window.tab_control.destroy()
    edit_window.overview.destroy()
    edit_window.suggest.destroy()
    edit_window.revisions.destroy()
    #search_frame.pack()

    # python = sys.executable
    # os.execl(python, python, *sys.argv)
    

# --MENU--

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New", command=new_file)  # edit from 'newpage'
submenu.add_command(label="Open", command=hello)
submenu.add_command(label="Save", command=hello)
submenu.add_command(label="Save As...", command=hello)
submenu.add_command(label="Recent files", command=hello)
submenu.add_command(label="Revert to last backup", command=hello)
submenu.add_separator()
submenu.add_command(label="Exit", command=window.quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=hello)
editmenu.add_command(label="Redo", command=hello)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)

viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="Toggle Text Box", command=hello)
viewmenu.add_command(label="Toggle Toolbar", command=hello)
viewmenu.add_command(label="Default Layout", command=hello)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Product Information", command=hello)
helpmenu.add_separator()
helpmenu.add_command(label="About...", command=hello)



def edit_window(article):
    edit_window.tab_control = ttk.Notebook(window)
    edit_window.overview = ttk.Frame(edit_window.tab_control)
    edit_window.suggest = ttk.Frame(edit_window.tab_control)  # make frame for suggestions ~~ !! print results
    edit_window.revisions = ttk.Frame(edit_window.tab_control)

    edit_window.tab_control.add(edit_window.overview, text='Overview')  # Add the tab
    edit_window.tab_control.add(edit_window.suggest, text='Suggestions')  # Add the tab
    edit_window.tab_control.add(edit_window.revisions, text='Revisions')  # Add the tab
    edit_window.tab_control.pack(fill='both', expand='yes')

    # if mouse hovers over line / sentence, the string is highlighted, clickable and copied to clipboard, etc
    editArea = ScrolledText(master=edit_window.overview, wrap=WORD, width=20, height=10, font="times 10")
    editArea.insert('1.0', article)
    editArea.pack(padx=10, pady=10, fill=BOTH, expand=True)

    lbl1 = Label(edit_window.suggest, text="suggest 1").pack()
    lbl2 = Label(edit_window.suggest, text="suggest 2").pack()
    lbl3 = Label(edit_window.suggest, text="suggest 3").pack()
    lbl4 = Label(edit_window.suggest, text="suggest 4").pack()

    xlbl1 = Label(edit_window.revisions, text="revisions 1").pack()
    xlbl2 = Label(edit_window.revisions, text="revisions 2").pack()
    xlbl3 = Label(edit_window.revisions, text="revisions 3").pack()
    xlbl4 = Label(edit_window.revisions, text="revisions 4").pack()

    # frame ??

    notes = Frame(window)
    notes.pack()

    # destroy edit window
    search_frame.destroy()




# main loop
def seed():
    window.mainloop()

# ~ RESOURCES ~

# can I put this to good use ?? !!!!!!!!!!!! https://www.kaggle.com/therohk/million-headlines
# multiple essay mode??? , expand windows and frames; full writing blueprint-cad style
# how to have something loop once

# ~~examples~~
# https://github.com/llSourcell/AI_Writer
# https://wordai.com/

# ~~tutorials~~
# https://www.youtube.com/watch?v=U_5V2dcTemk || EssayBot Creating a blog article in a few minutes, using AI-based writ
# https://www.youtube.com/watch?v=x24VEUEph0Q&feature=youtu.be || Build an AI Writer - Machine Learning for Hackers #8
# https://www.youtube.com/watch?v=8ypnLjwpzK8 || OpenAI GPT-2: An Almost Too Good Text Generator
# https://www.youtube.com/watch?v=0n95f-eqZdw || OpenAI Text Generator
# https://www.youtube.com/watch?v=a6fIbtFB46g
# https://stackoverflow.com/questions/18052395/array-of-buttons-in-python || creating an array of buttons

# ~~web scraping tests~~
# https://www.youtube.com/watch?v=a6fIbtFB46g&t=155s
