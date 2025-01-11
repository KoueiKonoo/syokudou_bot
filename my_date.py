#!/usr/bin/env python3
from datetime import datetime
import time
import threading

class MyDate:
    def __init__(self):
        self.update()

    def update(self):
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second

        date_list = []
        time_list = []

        for _ in [year, month, day]:
            if _ == month or _ == day:
                date_list.append(str(_).zfill(2))
            else:
                date_list.append(str(_))

        for _ in [hour, minute, second]:
            time_list.append(str(_).zfill(2))

        self.now_date = "/".join(date_list)
        self.now_time = ":".join(time_list)

    def monitor_date_change(self, interval=60):
        while True:
            now = datetime.now()
            new_date = f"{now.year}/{str(now.month).zfill(2)}/{str(now.day).zfill(2)}"
            if new_date != self.now_date:
                print(f"Date changed from {self.now_date} to {new_date}")
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