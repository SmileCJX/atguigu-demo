import wx

class MyFrame(wx.Frame):
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




if __name__ == "__main__":
    # 创建应用程序对象
    app = wx.App()
    # 创建窗口
    frm = MyFrame()
    # 显示窗口
    frm.Show()
    # 一直显示
    app.MainLoop()