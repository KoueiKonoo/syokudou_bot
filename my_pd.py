import pandas as pd
from my_date import MyDate
import threading
import time

class MyPandas():
    def __init__(self):
        self.data = "menu_data_with_items.xlsx"
        self.data_reload_thread = None
        self.start_data_reload(interval=120)  # 2分（120秒）ごとにデータを再読み込み
        self.update()
    
    def update(self):
        self.loaded_data = pd.read_excel(self.data, engine='openpyxl')
        self.my_date = MyDate()

    def get_menu_for_today(self):
        return self.get_menu_for_next_days(0)
    
    def get_menu_for_next_days(self,day):
        self.update()
        target_date = self.my_date.get_next_days(day)
        return self.get_menu_to_list(target_date)

    def get_menu_to_list(self, target_date):
        date = self.loaded_data["日付"].tolist()
        menu = None  # menu変数を初期化
        for i in range(len(date)):
            if date[i] == target_date:
                menu = self.loaded_data.iloc[i]
                break  # 一致する日付が見つかったらループを抜ける
        if menu is None or menu[1:].empty:
            return
        else:
            return menu[1:].tolist()

    def start_data_reload(self, interval=120):
        if self.data_reload_thread is None:
            def reload_loop():
                while True:
                    try:
                        self.update()
                    except Exception as e:
                        print(f"Failed to reload data: {e}")
                    print(f"Data reloaded at {(self.my_date.now_time).strftime('%H:%M:%S')}")
                    time.sleep(interval)
            self.data_reload_thread = threading.Thread(target=reload_loop)
            self.data_reload_thread.daemon = True
            self.data_reload_thread.start()


