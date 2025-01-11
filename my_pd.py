import pandas as pd
from my_date import MyDate
from discord.ext import commands

data = "menu_data_with_items.xlsx"

class MyPandas():
    def __init__(self, data):
        self.data = pd.read_excel(data)





