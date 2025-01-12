#!/usr/bin/env python3
import pandas as pd
import my_date
import threading
import time

data = "menu_data_with_items.xlsx"

class MyPandas(my_date.MyDate):
    def __init__(self, data):
        self.data = data
        self.loaded_data = pd.read_excel(data, engine='openpyxl')
        self.my_date = my_date.MyDate()
        self.start_data_reload(interval=86400)

    def get_menu_for_today(self):
        self.my_date.update()
        today_date = self.my_date.now_date
        date = self.loaded_data["日付"].tolist()
        menu = None  # menu変数を初期化
        for i in range(len(date)):
            if date[i] == today_date:
                menu = self.loaded_data.iloc[i]
                break  # 一致する日付が見つかったらループを抜ける
        if menu is None or menu[1:].empty:
            return ["本日のメニューはありません"]
        else:
            return menu[1:].tolist()

    def reload_data(self):
        self.loaded_data = pd.read_excel(self.data, engine='openpyxl')
        print("Data reloaded")

    def start_data_reload(self, interval=86400):
        def reload_loop():
            while True:
                self.reload_data()
                time.sleep(interval)
        thread = threading.Thread(target=reload_loop)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    my_pandas = MyPandas(data)
    while True:
        time.sleep(1)