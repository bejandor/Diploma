import matplotlib.pyplot as plt
import pandas as pd


#
# df1 = pd.read_excel('file1.xlsx')  # Читаем файл №1
# df2 = pd.read_excel('file2.xlsx')  # Читаем файл №2


# def drow_graphic():
    # Пишем функцию которая бы рисовала график
df1 = pd.read_excel('file1.xlsx')  # Читаем файл №1
df2 = pd.read_excel('file2.xlsx')  # Читаем файл №2

""" При выборе INNER JOIN (вид по умолчанию в SQL и pandas)
 объединяются только те значения, которые можно найти в обеих таблицах"""

result1 = pd.merge(df1, df2, on=["year", "month", "day", "hour", "min"], how="inner")

result1['mpv_difference'] = result1['mpv_x'] - result1['mpv_y']  # Выводим разницу

# Линейный график
# gca stands for 'get current axis'

# df1.plot(kind='line', x='author', y='mpv', ax=ax)
# df2.plot(kind='line', x='author', y='mpv', color='red', ax=ax)

result1.plot(kind='line', y='mpv_difference', color='red')

# if __name__ == "__main__":
#     drow_graphic()
