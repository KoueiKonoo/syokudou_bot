#!/usr/bin/env python3
import numpy as np
import pandas as pd
import my_date
from discord.ext import commands

data = "menu_data_with_items.xlsx"

class MyPandas(my_date.MyDate):
    def __init__(self, data):
        self.data = pd.read_excel(data, engine='openpyxl')
        self.my_date = my_date.MyDate()

    def get_menu_for_today(self):
        today_date = self.my_date.now_date
        date = self.data["日付"].tolist()
        menu = None  # menu変数を初期化
        for i in range(len(date)):
            if date[i] == today_date:
                menu = self.data.iloc[i]
                break  # 一致する日付が見つかったらループを抜ける
        if menu is None or menu[1:].empty:
            return ["本日のメニューはありません"]
        else:
            return menu[1:].tolist()

if __name__ == "__main__":
    my_pandas = MyPandas(data)
    menu = my_pandas.get_menu_for_today()
    print(menu)