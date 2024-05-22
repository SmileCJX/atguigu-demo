import wx

class MyFrame(wx.Frame):

    pos_x, pos_y = 10, 70
    btn_w, btn_h = 50, 50

    # 构造方法
    def __init__(self):
        # 创建窗口
        wx.Frame.__init__(self
                          , None
                          , title = "简单计算器"
                          , pos = (100, 100)
                          , size = (500, 800))
        # 创建面板
        self.pl = wx.Panel(self, pos = (0, 0), size = (500, 800))
        # 创建文本框
        self.entry = wx.TextCtrl(self.pl, pos = (10, 10), size = (400, 50), style = wx.TE_RIGHT)
        # 创建按钮
        # 第一行的四个按钮
        self.btn_clear = wx.Button(self.pl, label='C', pos = (self.pos_x, self.pos_y), size = (self.btn_w, self.btn_h))
        self.btn_div = wx.Button(self.pl, label='/', pos = (self.pos_x + 60, self.pos_y), size = (self.btn_w, self.btn_h))
        self.btn_mul = wx.Button(self.pl, label='*', pos = (self.pos_x + 120, self.pos_y), size = (self.btn_w, self.btn_h))
        self.btn_back = wx.Button(self.pl, label='<-', pos = (self.pos_x + 180, self.pos_y), size = (self.btn_w, self.btn_h))
        # 第二行的四个按钮
        self.btn_7 = wx.Button(self.pl, label='7', pos = (self.pos_x, self.pos_y + 60), size = (self.btn_w, self.btn_h))
        self.btn_8 = wx.Button(self.pl, label='8', pos = (self.pos_x + 60, self.pos_y + 60), size = (self.btn_w, self.btn_h))
        self.btn_9 = wx.Button(self.pl, label='9', pos = (self.pos_x + 120, self.pos_y + 60), size = (self.btn_w, self.btn_h))
        self.btn_sub = wx.Button(self.pl, label='-', pos = (self.pos_x + 180, self.pos_y + 60), size = (self.btn_w, self.btn_h))
        # 第三行的四个按钮
        self.btn_4 = wx.Button(self.pl, label='4', pos = (self.pos_x, self.pos_y + 120), size = (self.btn_w, self.btn_h))
        self.btn_5 = wx.Button(self.pl, label='5', pos = (self.pos_x + 60, self.pos_y + 120), size = (self.btn_w, self.btn_h))
        self.btn_6 = wx.Button(self.pl, label='6', pos = (self.pos_x + 120, self.pos_y + 120), size = (self.btn_w, self.btn_h))
        self.btn_add = wx.Button(self.pl, label='+', pos = (self.pos_x + 180, self.pos_y + 120), size = (self.btn_w, self.btn_h))
        # 第四行的四个按钮
        self.btn_1 = wx.Button(self.pl, label='1', pos = (self.pos_x, self.pos_y + 180), size = (self.btn_w, self.btn_h))
        self.btn_2 = wx.Button(self.pl, label='2', pos = (self.pos_x + 60, self.pos_y + 180), size = (self.btn_w, self.btn_h))
        self.btn_3 = wx.Button(self.pl, label='3', pos = (self.pos_x + 120, self.pos_y + 180), size = (self.btn_w, self.btn_h))
        self.btn_eq = wx.Button(self.pl, label='=', pos = (self.pos_x + 180, self.pos_y + 180), size = (self.btn_w, self.btn_h))
        # 第五行的两个按钮
        self.btn_0 = wx.Button(self.pl, label='0', pos = (self.pos_x, self.pos_y + 240), size = (self.btn_w, self.btn_h))
        self.btn_point = wx.Button(self.pl, label='.', pos = (self.pos_x + 180, self.pos_y + 240), size = (self.btn_w, self.btn_h))

if __name__ == "__main__":
    # 创建应用程序对象
    app = wx.App()
    # 创建窗口
    frm = MyFrame()
    # 显示窗口
    frm.Show()
    # 一直显示
    app.MainLoop()