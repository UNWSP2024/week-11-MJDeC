import tkinter as tk
import tkinter.messagebox

class GUI:
    def __init__(self) :
        self.main_window=tk.Tk()
        self.main_window.title('Information')

        self.info_button=tk.Button(self.main_window,text='Show Info',command=self.display_info)

        self.quit_button=tk.Button(self.main_window,text='Quit',command=self.main_window.destroy)

        self.quit_button.pack(side='left')
        self.info_button.pack(side='right')

        tk.mainloop()
        
    def display_info(self):
        tk.messagebox.showinfo('Information Display', 'Micah DeCaro\n618 Rice St. W\nStillwater,MN 55082')

if __name__ == '__main__':
    info=GUI()
