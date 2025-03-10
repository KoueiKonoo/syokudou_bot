#!/usr/bin/env python3
from datetime import datetime, timedelta
import time
import threading

class MyDate:
    def __init__(self):
        self.update()

    def update(self):
        self.now_date= datetime.now()
        self.now_time = datetime.now()
    
    def get_next_days(self, day):
        next_date = self.now_date + timedelta(days=day)
        return next_date.strftime("%Y/%m/%d")

    def monitor_date_change(self, interval=60):
        while True:
            new_date = self.now_date.strftime("%Y/%m/%d")
            if new_date != self.now_date:
                print(f"Date changed from {(self.now_date).strftime("%Y/%m/%d")} to {new_date}")
                self.update()  # 日付が変わった時に更新する
            time.sleep(interval)

    def start_monitoring(self, interval=60):
        thread = threading.Thread(target=self.monitor_date_change, args=(interval,))
        thread.daemon = True  # メインスレッドが終了するときにこのスレッドも終了するように設定
        thread.start()

# テスト用コード
if __name__ == "__main__":
    my_date = MyDate()
    my_date.start_monitoring(interval=10)  # 10秒ごとに日付を監視

    # メインスレッドが終了しないように待機
    while True:
        time.sleep(1)