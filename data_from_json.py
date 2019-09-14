#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import demjson


def clear():
    input_text.delete('0.0', 'end')
    output_text.delete('0.0', 'end')
    get_path_entry.delete('0', 'end')


def get_data():
    # 获取输入的json数据
    input_json = input_text.get("0.0", "end")
    try:
        decode_json = demjson.decode(input_json)
    except:
        output_text.delete('0.0', 'end')
        output_text.insert('end', ' json解析错误 ')
        return
    # 获取数据提取路径
    data_path = get_path_entry.get()
    temp = 'json' + str(data_path)
    repl = "output_data = " + temp
    print(repl)
    exec_to_get = """
if type(decode_json) == type([]):
    output_text.delete('0.0', 'end')
    for json in decode_json:
        try:
            here_will_be_replaced
        except:
            output_data = ' 路径解析错误 '
        finally:
            output_data = str(output_data) + '\\n'
            output_text.insert('end', str(output_data))
else:
    output_text.delete('0.0', 'end')
    try:
        here_will_be_replaced
    except:
        output_data = ' 路径解析错误 '
    finally:
        output_text.insert('end', str(output_data))
"""
    exec_to_get = exec_to_get.replace('here_will_be_replaced', repl)    # 通过替换来变成正确代码
    # print(exec_to_get)
    exec(exec_to_get)       # 将字符串作为代码执行


## 图形界面部分
window = tk.Tk()
window.title("data_from_json     by:MrWQ     https://github.com/MrWQ")

# 声明部件
# input_name = tk.Label(window, text='json')
input_text = tk.Text(window, width=80, height=15)
output_text = tk.Text(window, width=80, height=15)
change_frame = tk.LabelFrame(window, height=200, width=300, text='选择游戏')
get_path_entry = tk.Entry(change_frame, width=50)
get_data_button = tk.Button(change_frame, text='get data', width=10, height=1, compound='left', command=get_data)
reset_button = tk.Button(change_frame, text='clear all', width=10, height=1, compound='left', command=clear)

# 设置部件文字
input_text.insert('insert', '[{a:1, b:2, "c":3, "d":"4"},{a:"a", "c":"c"}]')
get_path_entry.insert('insert', '["a"]')
output_text.insert('insert', 'data will output here')

# 设置部件位置
input_text.pack(padx=10, pady=10, fill='both', side='top', expand=True)
change_frame.pack(padx=10, fill='x')
output_text.pack(padx=10, pady=10, fill='both', expand=True)

get_path_entry.grid(padx=10, pady=10, row=0, column=0, sticky=tk.E+tk.W)
get_data_button.grid(padx=10, pady=10, row=0, column=1, sticky=tk.E+tk.W)
reset_button.grid(padx=10, pady=10, row=0, column=2, sticky=tk.E+tk.W)

window.mainloop()