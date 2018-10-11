import tkinter;

top = tkinter.Tk();
top.title("列表");
top.geometry("400x300");

varListboxValue = tkinter.StringVar();
varListboxValue.set((12,23,34,45,56));
listBox1 = tkinter.Listbox(top, listvariable=varListboxValue);
listBox1.pack();

nums = list(range(20));
for num in nums:
	listBox1.insert("end", num);
listBox1.insert(0, "第零");
listBox1.insert(1, "第一");
listBox1.insert(2, "第二");
listBox1.insert(3, "第三");
listBox1.delete(3);


def printSelection():
	selectIdx = listBox1.curselection();
	print(selectIdx);
	selectVal = listBox1.get(selectIdx);
	#txt.delete("1.0", "end");
	txt.insert("end", selectVal);

printBtn = tkinter.Button(top, text="print selection", width=15, height=3, command=printSelection);
printBtn.pack();

txt = tkinter.Text(top, height=5, width=100);
txt.pack();

top.mainloop();


