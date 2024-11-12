import tkinter as tk  

def gui():  
    window=tk.Tk()  
    window.title("Favorite Quote")  
  
    tk.Label(window,text='"Innovation distinguishes between a leader and a follower."\n(said by Steve Jobs)',padx=10000,pady=200,font=("Comfortaa", 41),justify="center").pack()  

    window.mainloop()  

if __name__ == "__main__":  
    gui()
