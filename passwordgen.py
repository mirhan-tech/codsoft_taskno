from tkinter import *
import tkinter.messagebox as msg
import random
import re
from termcolor import colored

class PasswordGenerator(Tk):

    def __init__(self):
        super().__init__()
        # Centering the window when opened.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        app_width = 500
        app_height = 280
        set_x = int((screen_width / 2) - (app_width / 2))
        set_y = int((screen_height / 2) - (app_height / 2))
        self.geometry(f'{app_width}x{app_height}+{set_x}+{set_y}')
        self.title("Password Generator")
        self.resizable(False, False)
        # application design
        self.app_heading_frame = self.create_app_heading_frame()
        self.create_heading_label()
        self.length_input_frame = self.create_length_input_frame()
        self.create_password_length_label()
        self.password_length_entry = self.create_password_length_entry()
        self.strength_input_frame = self.create_strength_input_frame()
        self.create_password_strength_label()
        self.choice = StringVar()
        self.choice.set("high")
        self.create_strength_radio_options()
        self.button_frame = self.create_button_frame()
        self.create_generate_button()

    def create_app_heading_frame(self):
        frame = Frame(self, height = 50, bg = "#2b2e30")
        frame.pack(fill = X)
        return frame

    def create_heading_label(self):
        label = Label(self.app_heading_frame, text = "Password Generator", font = ("Helvetica", 23, "bold"), fg = "#b1ccea", bg = "#2b2e30")
        label.pack()

    def create_length_input_frame(self):
        frame = Frame(self, bg = "#e5e7ea", height = 300, padx = 20, pady = 20)
        frame.pack(fill = BOTH)
        return frame

    def create_password_length_label(self):
        label = Label(self.length_input_frame, text = "Set password length", font = ("Helvetica", 16), bg = "#e5e7ea", fg = "#1a0944")
        label.pack(side = LEFT, padx = (0, 10))

    def create_password_length_entry(self):
        entry = Entry(self.length_input_frame, width = 3, fg = "#1e4976", font = ("Helvetica", 13))
        entry.pack(side = LEFT,  ipady = 2, ipadx = 2)
        return entry

    def create_strength_input_frame(self):
        
        frame = Frame(self, bg = "#e5e7ea", height = 300, padx = 20, pady = 20)
        frame.pack(fill = BOTH)
        return frame

    def create_password_strength_label(self):
       
        label = Label(self.strength_input_frame, text = "Set password strength", font = ("Helvetica", 16), bg = "#e5e7ea", fg = "#1a0944")
        label.pack(anchor = W)

    def create_strength_radio_options(self):
       
        option1 = Radiobutton(self.strength_input_frame, text = "low", value = "low", variable = self.choice, font = ("Helvetica", 13), bg = "#e5e7ea")
        option2 = Radiobutton(self.strength_input_frame, text = "medium", value = "medium", variable = self.choice, font = ("Helvetica", 13), bg = "#e5e7ea")
        option3 = Radiobutton(self.strength_input_frame, text = "high", value = "high", variable = self.choice, font = ("Helvetica", 13), bg = "#e5e7ea")
        option1.pack(side = LEFT, padx = (50, 0))
        option2.pack(side = LEFT, padx = (50, 0))
        option3.pack(side = LEFT, padx = (50, 0))

    def create_button_frame(self):
        
        frame = Frame(self, bg="#e5e7ea", height=100, padx=20, pady=20)
        frame.pack(fill=BOTH)
        return frame

    def show_generate_password_window(self, length, strength, password):
        
        show_generated_password_popup_window = Toplevel(self)
        show_generated_password_popup_window.geometry("700x215")
        show_generated_password_popup_window.resizable(False, False)
        show_generated_password_popup_window.title(f"Your Generated Password")
        label = Label(show_generated_password_popup_window, text = f"GENERATED PASSWORD\nLENGTH: {length}\tSTRENGTH: {strength}", fg = "#1d3b64", font = ("Helvetica", 16))
        label.pack()
        pass_view = Text(show_generated_password_popup_window, height = 3, width = 70, fg = "#1d3b64", bg = "#e5e7ea", font = ("Helvetica", 13))
        pass_view.insert(END, password)
        pass_view.config(state = DISABLED)
        pass_view.pack()
        btn_close = Button(show_generated_password_popup_window, text = "Close", width = 13, bd = 0, bg = "#3c8bdf", fg = "#ffffff", font = ("Helvetica", 13, "bold"), command = show_generated_password_popup_window.destroy)
        btn_close.pack(side = RIGHT, padx = (0, 20))
        show_generated_password_popup_window.mainloop()


    def create_generate_button(self):
        
        button = Button(self.button_frame, text = "GENERATE", bg = "#235d48", fg = "#e1e6e4", borderwidth = 0, cursor = "hand2", padx = 20, pady = 5, command = lambda: self.collect_password(self.password_length_entry.get(), self.choice.get()))
        button.pack()

    def generate_low_security_password(self, length):
        
        low_pass_char = list()
        for c in range(65, 90):
            low_pass_char.append(chr(c))
        for s in range(97, 122):
            low_pass_char.append(chr(s))
        l = 1
        p = ""
        while l <= length:
            choice = random.choice(low_pass_char)
            p += choice
            l += 1
        print(colored(f"Generated password : {p}", "light_green"))
        return p

    def generate_medium_security_password(self, length):
       
        med_pass_char = list()
        for c in range(65, 91):
            med_pass_char.append(chr(c))
        for n in range(48, 58):
            med_pass_char.append(chr(n))
        for s in range(97, 123):
            med_pass_char.append(chr(s))
        l = 1
        p = ""
        while l <= length:
            choice = random.choice(med_pass_char)
            p += choice
            l += 1
        # Make sure that the generated password has integers.
        # Checking if the generated password contains any integers or not.
        check_int = re.compile('[0123456789]')
        if check_int.search(p) is None:
            p = self.generate_medium_security_password(length)
        elif check_int.search(p) is not None:
            print(colored(f"Generated password : {p}", "light_green"))
        return p

    def generate_high_security_password(self, length):
        
        high_pass_char = list()
        sp_chr = ['!', '@', '#', '$', '%', '^', '&', '*']
        for c in range(65, 91):
            high_pass_char.append(chr(c))
        for n in range(48, 58):
            high_pass_char.append(str(n))
        for sp in sp_chr:
            high_pass_char.append(sp)
        for s in range(97, 123):
            high_pass_char.append(chr(s))
        l = 1
        p = ""
        while l <= length:
            choice = random.choice(high_pass_char)
            p += choice
            l += 1
        # Make sure that the generated password has numbers and special characters both.
        # Checking if the generated password contains any integer and special character.
        check_sp = re.compile('[!@#$^&*]')
        check_int = re.compile('[0123456789]')
        if check_sp.search(p) is None and check_int.search(p) is None:
            p = self.generate_high_security_password(length)
        elif check_sp.search(p) is None and check_int.search(p) is not None:
            p = self.generate_high_security_password(length)
        elif check_sp.search(p) is not None and check_int.search(p) is None:
            p = self.generate_high_security_password(length)
        elif check_sp.search(p) is not None and check_int.search(p) is not None:
            print(colored(f"Generated password : {p}", "light_green"))
        return p

    def collect_password(self, length, strength):
       
        try:
            length = int(length)
            if length > 80 or length < 4:
                msg.showwarning(title = "WARNING",message = "password length must be less than 81 and greater than 3")
            elif length <= 80 or length >= 4:
                print(colored(f"Starting password generation:\nLength = {length} Strength = {strength}", "light_blue"))
                if strength == "low":
                    password = self.generate_low_security_password(int(length))
                    self.show_generate_password_window(length, strength, password)
                elif strength == "medium":
                    password = self.generate_medium_security_password(int(length))
                    self.show_generate_password_window(length, strength, password)
                elif strength == "high":
                    password = self.generate_high_security_password(int(length))
                    self.show_generate_password_window(length, strength, password)
        except Exception as e:
            print(colored(f"Exception : {e}", "red"))
            msg.showwarning(title = "WARNING", message = "invalid password length\n(minimum 4 | maximum 80)")


    def run(self):
        
        self.mainloop()

if __name__ == '__main__':
    app = PasswordGenerator()
    app.run()
