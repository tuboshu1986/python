import tkinter;

top = tkinter.Tk();

helloLabel = tkinter.Label(top, text="Hello 小明 !!");
helloLabel.pack();

quitBtn = tkinter.Button(top, text="退出", command=top.quit, bg="red", fg="blue");
quitBtn.pack(fill=tkinter.X, expand=1);

tkinter.mainloop();
