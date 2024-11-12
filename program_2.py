import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self) :
        self.main_window=tkinter.Tk()
        self.main_window.title('Info')

        self.info_button=tkinter.Button(self.main_window,text='Show Info',command=self.display_info)

        self.quit_button=tkinter.messagebox(self.main_window,text='Quit',command= self.main_window.destroy)

        self.quit_button.pack(side='right')
        self.info_button.pack(side='left')

        tkinter.mainloop()
    def display_info(self):
        tkinter.messagebox.showinfo('Information Display', 'Micah DeCaro','618 Rice St. W','Stillwater,MN 55082')

if __name__ == '__main__':
    info=GUI()
    
