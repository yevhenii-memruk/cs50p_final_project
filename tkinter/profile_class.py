import tkinter as tk
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk
from mss import mss


class BasePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label_bkgr = tk.Label(self, image=controller.bgimg)

class TimeChecker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.resizable(width=False, height=False)
        self.title("Time Tracker")

        # Setting background
        self.bgimg = tk.PhotoImage(file=r"tkinter\background.png")
        label_bg = tk.Label(self, i=self.bgimg)
        label_bg.pack()

        # Screen Shot
        take_screenshot = tk.Button(self, text="📸", command=self.screen_shot)
        take_screenshot.place(x=655, y=1)

        # Track Single app
        self.options_list_single_app = [ 
            "Google", 
            "Python", 
            "VS Code", 
            "Pycharm", 
            "Telegram"
        ]

        text_tracking_single_app = tk.Label(self, 
        text="Choose the app you want to track", 
        font=("Roboto", 16, "bold"))
        text_tracking_single_app.place(x=250, y=180)

        ## drop down menu
        self.clicked = tk.StringVar() 
        self.clicked.set("Apps List:")
        drop = tk.OptionMenu(self, self.clicked, *self.options_list_single_app, command=self.get_track_app)
        drop.place(x=350, y=220)

        ## button of refresh data list
        button_data_app = tk.Button(self, text="🔁", command=self.refresh_list_apps)
        button_data_app.place(x=450, y=223)

        ## Empty line - holder
        self.data_of_app = tk.Label(self, 
        text="\t\t\t\t\t",
        font=("Roboto", 14, "bold"),
        relief="solid")
        self.data_of_app.place(x=210, y=270) 

        # Photo Adjustment 
        file_explorer = tk.Label(self, text="Photo",
        font=("Verdana", 14, "bold"),
        width=10,
        height=8, fg="white", bg="grey")
        file_explorer.place(x=7, y=4)

        button_photo = tk.Button(self, text="Edit Photo", 
        width=11, 
        font=("Roboto", 14),
        command=self.browse)
        button_photo.place(x=9, y=200)

        # Username Adjustment 
        self.edit_cheker_for_name = 0

        username = tk.Label(self, text="Username:", font=("Verdana", 8))
        username.place(x=9, y=250)

        button_username = tk.Button(self, text="🖊️",
        height=1, 
        command=self.name_edit, 
        wraplength=1)
        button_username.place(x=113, y=252)

        self.entry_name = tk.Entry(self, width=21)
        self.entry_name.insert(0, "None")
        self.entry_name.configure(state="disabled")
        self.entry_name.place(x=9, y=270)

        # Top 3 active apps
        top_3_apps_text = tk.Label(self, text="Top 3 Apps", 
        font=("Verdana", 20, "bold"))
        top_3_apps_text.place(x=330, y=5)

        self.top3_last_week_apps = ["Google:  20 hours for last week", 
                                    "VS Code: 10 hours for last week",
                                    "Apple:  31 hours for last week"]
    
        var = tk.Variable(value=self.top3_last_week_apps)

        list_tip3_apps = tk.Listbox(self, listvariable=var, height = 3, 
        width = 30, 
        activestyle = 'dotbox', 
        font = ("Verdana", 20))
        list_tip3_apps.place(x=166, y=50)

        # Get info for today
        button_get_for_today = tk.Button(self,
        text="Get info for Today", 
        command=self.get_info_button, 
        font=("Verdana", 16))
        button_get_for_today.place(x=250, y=340)

        # SYNC button
        button_sync_app = tk.Button(self, text="SYNC", command=self.sync_app)
        button_sync_app.place(x=160, y=270)

        # EXIT Window, just in case I want to do something before closing
        self.protocol("WM_DELETE_WINDOW", self.exit)     

    def exit(self):
        self.destroy()

    def browse(self):
        f_path = askopenfilename(title="Select File", filetypes=([("All Files","*.*")]))
        img = Image.open(f_path)
        img = img.resize((132, 195))
        img = ImageTk.PhotoImage(img)
        e1 = tk.Label(self)
        e1.place(x=8, y=0)
        e1.image = img
        e1["image"] = img

    def name_edit(self):
        if self.edit_cheker_for_name:
            self.entry_name.configure(state="disabled")
            self.edit_cheker_for_name = 0
        else: 
            self.entry_name.configure(state="normal", bg="#e6818c")
            self.edit_cheker_for_name = 1

    def screen_shot(self):
        with mss() as sct:
            filename = sct.shot(mon=-1, output="tkinter\screenshots\screenshot.png")

    def get_track_app(self, *args):
        if self.clicked.get() == "Apps List:":
            pass
        else:
            self.data_of_app["text"] = self.clicked.get()

    def refresh_list_apps(self):
        pass

    def get_info_button(self):
        pass

    def sync_app(self):
        pass

        
if __name__ == "__main__":
    app = TimeChecker()
    app.mainloop()