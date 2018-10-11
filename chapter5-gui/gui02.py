import tkinter;

top = tkinter.Tk();
top.title("text");
top.geometry("400x300");

entry1 = tkinter.Entry(top, show=None, width=100);
entry1.pack();

def insertPoint():
	str = entry1.get();
	text1.insert("insert", str);
btn1 = tkinter.Button(top, text="insert point", width=15, height=2, command=insertPoint);
btn1.pack();

def insertEnd():
	str = entry1.get();
	text1.insert("end", str);
btn2 = tkinter.Button(top, text="insert end", width=15, height=2, command=insertEnd);
btn2.pack();

text1 = tkinter.Text(top, height=5);
text1.pack();


top.mainloop();

