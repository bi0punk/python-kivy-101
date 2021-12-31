
import requests
import json


from prettytable import PrettyTable
from os import read
from kivy.app import App
from kivy.uix.label import Label
import pandas as pd


class Earth(App):
    def build(self):
        x = PrettyTable()
        
        df = pd.read_json("https://api-sismologia-chile.herokuapp.com/")

        mag = df["magnitud"]
        ref = df["referencia"]

        x.field_names = ["MAGNITUD", "REFERENCIA GEOGRAFICA"]
        x.add_row([mag, ref])


        mystring = x.get_string()
    
       
        return Label(text = mystring)
Earth().run()