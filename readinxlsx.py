import pandas as pd
import json 
excel_data = pd.read_excel('book.xlsx', 'Big Cat')
data = pd.DataFrame(excel_data, columns=['书名', '系列'])


bookname = data.loc[:,'书名']
booklist = []
for book in bookname:
    booklist.append(book)
    

with open("booklist.json", "w") as outfile:
    json.dump(booklist,outfile, indent = 6)
    
print(booklist)