import twint
import schedule
import time
import csv

csv_file = open('input.csv')
input = []
for str in csv_file:
    str1 = str.split('\n',1)
    arr = str1[0].split(',')
    input.append(arr)


for list in input:
    str1 = "files/"+list[0]+".csv"
    str2 = ""
    for i in list[1:]:
        str2 = str2+i+" "
    # print(str1)
    # print(str2)
    c = twint.Config()
    c.Search = str2
    c.Limit = 1000
    c.Store_csv = True
    open(str1,"a")
    c.Output = str1
    c.Lang = "en"
    twint.run.Search(c)


# schedule.every().minute.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
