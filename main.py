import psutil
import time
import tkinter as tk
import ctypes
import threading

def getComputerStatus(resultDict):
    while 1:
        s1 = psutil.net_io_counters(pernic=True)['以太网']
        time.sleep(1)
        s2 = psutil.net_io_counters(pernic=True)['以太网']
        netStatus = str('实时网速：' + '%.2f' % ((s2.bytes_recv - s1.bytes_recv) / 1024)) + "kb/s"
        counts = "CPU物理核心数：" + str(psutil.cpu_count(logical=False))
        CPUStatus = psutil.cpu_percent(interval=1, percpu=False)
        cpuStatus = "CPU使用率：" + str(CPUStatus) + "%"
        resultDict['实时网速'] = netStatus
        resultDict['CPU物理核心数'] = counts
        resultDict['CPU使用率'] = cpuStatus

def updateWin():
    root.children['netStatus'].config(text=resultDict['实时网速'])
    root.children['cpuCounts'].config(text=resultDict['CPU物理核心数'])
    root.children['cpuStatus'].config(text=resultDict['CPU使用率'])
    root.after(10, updateWin)

if __name__ == '__main__':
    resultDict = {'实时网速': 'None', 'CPU物理核心数': 'None', 'CPU使用率': 'None'}
    p = threading.Thread(target=getComputerStatus, args=(resultDict, ))
    p.start()

    root = tk.Tk()
    root.title('myDemo')
    root.overrideredirect(True) # 无边框模式
    root.wm_attributes('-topmost', 1) # 窗口置顶

    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root.config(bg='#000000')

    label1 = tk.Label(name='netStatus', font=('Hack', 20, 'bold'), bg='#303030', fg='white').pack()
    label2 = tk.Label(name='cpuCounts', font=('Hack', 20, 'bold'), bg='#303030', fg='white').pack()
    label3 = tk.Label(name='cpuStatus', font=('Hack', 20, 'bold'), bg='#303030', fg='white').pack()
    label4 = tk.Label(name='imBobby', font=('Hack', 20, 'bold'), bg='#303030', fg='white', text="===imBobby的小工具===").pack()
    root.after(10, updateWin)

    root.mainloop()