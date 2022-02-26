# 把一个数组里的所有字符串遍历相乘，如果是字符的就记为1
# “123”=123
# “asss”=1
# “123asd”=1
# 类似于这样
# 举例：["123","2","asd"]
# 结果：246

str_list = ['2022', '2', '24', 'ETH', '2400', '俄羅斯開戰烏克蘭']
result = 1
for x in str_list :
    try :
        result *= float(x)
    except :
        print('無法直接轉換為float，以1計不影響最終結果')

print(f'result : {result}')