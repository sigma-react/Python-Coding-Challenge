from prettytable import PrettyTable
import numpy as np
import pandas as pd

table = PrettyTable()
table.field_names = ['id', 'name', 'price', 'expires']
global df

def display_table(value):
    """
    Display product table
    """

    min_price = np.where(float(value[0]), float(value[0]), df["price"].min())
    max_price = np.where(float(value[1]), float(value[1]), df["price"].max())
    mask1 = df['price'] >= min_price
    mask2 = df["price"] <= max_price
    try:
        expires_start = pd.to_datetime(value[2])
        expires_stop = pd.to_datetime(value[3])
        mask3 = df["expires"] >= expires_start
        mask4 = df["expires"] <= expires_stop
        data = df[(mask1 & mask2) & (mask3 & mask4)]
    except Exception as e:
        data = df[mask1 & mask2]
        print(e)
    for idx,row in data.iterrows():
        table.add_row([row['id'], row['name'], row['price'], row['expires']])
    print(table)
    table.clear_rows()


def start():
    """
    Start accepting user input
    Quit program when user types 'exit'
    """

    while True:
        value = input('> ')
        value = value.split(' ')
        if value[0] == 'exit':
            break
        display_table(value)


if __name__ == '__main__':
    df = pd.read_csv('products.csv')
    df['expires'] = pd.to_datetime(df['expires'])
    start()
