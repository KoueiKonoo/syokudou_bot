import pandas as pd
import my_date
import threading
import time

data = "menu_data_with_items.xlsx"

class MyPandas(my_date.MyDate):
    def __init__(self, data):
        self.data = data
        self.loaded_data = pd.read_excel(self.data, engine='openpyxl')
        self.my_date = my_date.MyDate()
        self.data_reload_thread = None
        self.start_data_reload(interval=120)  # 2分（120秒）ごとにデータを再読み込み

    def get_menu_for_today(self):
        self.my_date.update()  # 最新の日付を取得
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
    
    def get_menu_for_next_days(self,day):
        self.my_date.update()
        next_date = self.my_date.get_next_days(day)
        date = self.loaded_data["日付"].tolist()
        menu = None
        for i in range(len(date)):
            if date[i] == next_date:
                menu = self.loaded_data.iloc[i]
                break
        if menu is None or menu[1:].empty:
            return [f"{next_date}のメニューはありません"]
        else:
            return menu[1:].tolist()


    def reload_data(self):
        try:
            self.loaded_data = pd.read_excel(self.data, engine='openpyxl')
            self.my_date.update()
        except Exception as e:
            print(f"Failed to reload data: {e}")

    def start_data_reload(self, interval=120):
        if self.data_reload_thread is None:
            def reload_loop():
                while True:
                    self.reload_data()
                    print(f"Data reloaded at {self.my_date.now_time}")
                    time.sleep(interval)
            self.data_reload_thread = threading.Thread(target=reload_loop)
            self.data_reload_thread.daemon = True
            self.data_reload_thread.start()

if __name__ == "__main__":
    my_pandas = MyPandas(data)
    while True:
        time.sleep(1)