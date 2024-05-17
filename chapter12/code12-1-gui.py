import wx
# 创建应用程序对象
app = wx.App()
# 创建窗口
# size: 宽，高， pos（左上角）：x坐标，y坐标
frm = wx.Frame(None, size = (600, 800), pos = (100, 100))
# 显示窗口
frm.Show()
# 创建面板
pl = wx.Panel(frm, size = (400, 400), pos = (100, 100))

# 进入主循环，让窗口一直显示
app.MainLoop()