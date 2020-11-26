# 打开并读取文件
file = open(r'C:\Users\Administrator\Desktop\stu.csv','r')
lines = file.readlines()
# 给每行添加行号 如#1，#2
# 用#对齐
# 求最长行的长度
max_len = 0
for line in lines:
    if len(line) > max_len:
        max_len = len(line)
print(max_len)
line_num = 0
new_lines = []
for line in lines:
    line_num += 1
    tmp_line = line.rstrip().ljust(max_len+10) + '#' + str(line_num)
    new_lines.append(tmp_line)
new_lines