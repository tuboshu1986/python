import tkinter;

top = tkinter.Tk();
quitBtn = tkinter.Button(top, text="退出", command=top.quit);
quitBtn.pack();
tkinter.mainloop();
