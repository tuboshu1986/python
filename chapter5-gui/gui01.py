import tkinter;

top = tkinter.Tk();
top.title("gui01");
top.geometry("400x300");

varText = tkinter.StringVar();
varFlag = True;
def varBtnFunction():
	global varFlag;
	if(varFlag):
		varFlag = False;
		varText.set("我有万古宅，嵩阳玉女峰。");
	else:
		varFlag = True;
		varText.set("长留一片月，挂在东溪松。");

varLabel = tkinter.Label(top, textvariable=varText, bg="green", font=("Arial", 20), width=50, height=2);
varLabel.pack();

varBtn = tkinter.Button(top, text="修改var", width=10, height=2, command=varBtnFunction);
varBtn.pack();

top.mainloop();

