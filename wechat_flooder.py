# 最简单的微信刷屏程序
import time
from pynput import mouse, keyboard
from tqdm import tqdm
from pynput.keyboard import Key, Controller

s = int(input('发送次数：'))
word = str(input('在这里输入想发送的话：'))

print('预留5秒用于准备')
for i in tqdm(range(100)): # 在终端显示倒计时预留5秒用于准备
    time.sleep(0.05)

m_mouse = mouse.Controller()
m_keyboard = Controller()

# 请确保鼠标在聊天框内
m_mouse.click(mouse.Button.left)  # 点击鼠标左键，这里可要可不要

for a in tqdm(range(s)):  # 这里输入轰炸的次数
    # # 按下Ctrl键和v键
    # m_keyboard.press(Key.cmd) # 提前cmd c剪贴板的内容
    # m_keyboard.press('v')
    # # 释放Ctrl键和v键
    # m_keyboard.release(Key.cmd)
    # m_keyboard.release('v')

    m_keyboard.type(word)

    m_keyboard.press(Key.enter)  # 按下enter发送
    m_keyboard.release(Key.enter)  # 释放enter
    time.sleep(0.05)  # 这里调整频率(一次发送后的等待时间)

print('刷屏完成')



# 注意，如果想发送的话是中文+英文，比如“你好，hello”的话，键盘就是中文模式，所以需要多打一个回车。如果有多段英语的话同理。