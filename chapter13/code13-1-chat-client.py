import wx
from socket import *
import threading

class Client(wx.Frame):
    # 构造方法
    def __init__(self):
        # 实例属性
        self.name = 'cjx' # 客户端名字
        self.isConnectd = False # 客户端是否连接服务器
        self.client_socket = None

        # 界面布局
        wx.Frame.__init__(self, None, title = self.name + "聊天室客户端", size = (450, 600), pos = (100, 100))
        # 创建面板
        self.pl = wx.Panel(self)
        # 创建按钮
        # 加入聊天室
        self.conn_btn = wx.Button(self.pl, label = '加入聊天室', pos = (10, 10), size = (200, 40))
        # 离开聊天室

        # 清空按钮
        # 发送按钮

# 程序入口
if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建客户端窗口
    client = Client()
    # 显示客户端窗口
    client.Show()

    # 一直循环显示
    app.MainLoop()