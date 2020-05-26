import re
file_path = "Order_Reports__2017__2020_-_In_05-05-2020-12-15-09"
pattern = re.compile('\d{2}-\d{2}-\d{4}')
date = re.findall(pattern, file_path)
print(date[0])