from ctypes import alignment
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Treeview

from matplotlib.pyplot import text
import topOfTop as tot

class Application(Frame):

    def askOpenFilename(self, stringVar:StringVar):
        filename = filedialog.askopenfilename(filetypes=[("Excel file","*.xlsx"),("Excel file", "*.xls")])
        if len(filename) > 0:
            stringVar.set(filename)

    def submit(self):
        self.lists = tot.submitFile(self.premiumfilename.get(), self.basicfilename.get(), self.radiovalue.get())
        
        if len(self.lists) > 0:
            for i in range(len(self.lists)):
                self.table.insert('', 'end', text=1, values=self.lists[i])
        else:
            messagebox.showwarning('파일오류','파일 검색에 실패하였습니다.')

    def reset(self):
        self.lists = []
        for i in self.table.get_children():
            self.table.delete(i)
    
    def save(self):
        if len(self.lists) > 0:
            tot.saveFile(self.lists)
            messagebox.showinfo('저장완료','저장이 완료되었습니다.')
        else:
            messagebox.showwarning('정보오류','정보가 없습니다.')
        print("save")

    def filePremium(self):
        self.premiumfilename = StringVar()
        self.premiumfilename.set("파일을 입력하세요.")

        frame = Frame(self)
        frame.pack(pady=10)
        hi_there = Button(frame,text="프리미엄", command=lambda: self.askOpenFilename(self.premiumfilename))
        lbName = Label(frame, textvariable=self.premiumfilename)
        hi_there.pack(side='left')
        lbName.pack(side='left')

    def fileBasic(self):
        self.basicfilename = StringVar()
        self.basicfilename.set("파일을 입력하세요.")

        frame = Frame(self)
        frame.pack()
        hi_there = Button(frame,text="베이직", command=lambda: self.askOpenFilename(self.basicfilename))
        lbName = Label(frame, textvariable=self.basicfilename)
        hi_there.pack(side='left')
        lbName.pack(side='left')



    def fileSubmit(self):
        self.radiovalue = IntVar()

        frame = Frame(self)
        frame.pack()
        radio01 = Radiobutton(frame, text="총구매금액", variable=self.radiovalue, value=0)
        radio02 = Radiobutton(frame, text="순서2", variable=self.radiovalue, value=1)
        radio03 = Radiobutton(frame, text="순서3", variable=self.radiovalue, value=2)

        submit = Button(frame, text="검색", command=self.submit )
        reset = Button(frame, text="초기화", command=self.reset)
        seveBtn = Button(frame, text="저장", command=self.save)
        quitBtn = Button(frame,text="종료", fg="red", command=self.quit)

        radio01.pack(side=LEFT)
        radio02.pack(side=LEFT)
        radio03.pack(side=LEFT)
        
        submit.pack(side='left', padx=5)
        reset.pack(side='left')
        seveBtn.pack(side='left', padx=5)
        quitBtn.pack(side='left')
        

    def tableFrame(self):
        headerName = ["구매자명", "프리미엄", "수량", "구매금액"," 베이직", "수량", "구매금액" ,"총구매금액"]
        frame = Frame(self)
        frame.pack(fill=X, pady=10)
        self.table = Treeview(frame, column=headerName, show='headings')
        for i in range(len(headerName)):
            self.table.heading("# {0}".format(i+1), text=headerName[i])
            self.table.column("# {0}".format(i+1), width=60)
        self.table.pack(side='left')
        vsb = Scrollbar(frame, orient='vertical', command=self.table.yview)
        vsb.pack(side='right', fill='y')
        self.table.configure(yscrollcommand=vsb.set)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.filePremium()
        self.fileBasic()
        self.fileSubmit()
        self.tableFrame()

root = Tk()
root.title("SHOE CAVE CHALLENGER [v0.4.3]")
app = Application(master=root)
app.mainloop()
