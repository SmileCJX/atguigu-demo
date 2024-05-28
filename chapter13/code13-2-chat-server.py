import wx
from socket import *
import threading
from concurrent.futures import ThreadPoolExecutor

class Server(wx.Frame):
    def __init__(self):
        # 实例属性
        self.isOn = False # 表示服务器的启动状态
        # 创建socket对象
        self.server_socket = socket()
        # 绑定ip地址和端口号
        self.server_socket.bind(('0.0.0.0',8999))
        # 监听
        self.server_socket.listen(5)

        # 界面布局的操作
        # 调用父类的init方法
        wx.Frame.__init__(self, None, title = '多人聊天室', pos = (0, 50), size = (450, 600))
        # 创建面板
        self.pl = wx.Panel(self)
        # 创建按钮
        start_server_btn = wx.Button(self.pl, pos = (10, 10), size = (200, 40), label = '启动服务器')
        # 启动服务器
        # 保存聊天记录
        save_text_btn = wx.Button(self.pl, pos = (220, 10), size = (200, 40), label = '保存聊天记录')
        # 创建聊天内容文本框
        self.text = wx.TextCtrl(self.pl, size=(400, 400), pos=(10, 60), style=wx.TE_READONLY|wx.TE_MULTILINE)
        # 给按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.start_server, start_server_btn)
        self.Bind(wx.EVT_BUTTON, self.save_text, save_text_btn)

    # 启动服务器
    def start_server(self, event):
        print('start server')

    # 保存聊天记录
    def save_text(self, event):
        print("save text")

# 程序入口
if __name__ == '__main__':
    # 创建应用程序对象
    app = wx.App()
    # 创建服务器的窗口
    server = Server()
    # 显示服务器窗口
    server.Show()
    # 循环显示
    app.MainLoop()