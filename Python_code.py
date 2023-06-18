##產生題目
#函數設置 and 導入模組
import random
string = ""

#設置產生數字的迴圈，使其產生4位不重複的數字，並加入string字串
while len(string) < 4:
    Test = random.randint(0,9)
    if str(Test) in string:
        continue
    if str(Test) not in string:
        string += str(Test)

## 設定玩家猜題的輸入
#函數設置 and 導入numpy模組
from numpy import char
GUESS_string = ""
Test_number = 8
Test_limits = True
count = 0
a = 0
b = 0


while Test_limits:
    GUESS_string = input("請輸入4個不重複的4位數字: ")
    if len(set(GUESS_string)) != 4 or len(set(GUESS_string)) != len(GUESS_string) or not char.isnumeric(GUESS_string):
        print("輸入錯誤，請重新輸入\'4個不重複的4位數字\'")
        continue
            #設定玩家如果輸入不是"4個不重複的4位數字"則重新輸入
    if len(set(GUESS_string)) == 4:
        count += 1 #如果輸入4個不重複的4位數字 才計算猜測次數
    if GUESS_string == string:
            print("恭喜你答對了") #假如猜對則直接跳出迴圈並顯示答對
            break
    if GUESS_string != string: #假如沒猜對才執行以下的計算
        for i in range(len(GUESS_string)):
            if GUESS_string[i] == string[i]:
                a += 1
            if GUESS_string[i] != string[i] and GUESS_string[i] in string:
                b += 1
                #計算猜測的數字有幾個A(數字位置正確)幾個B(數字正確位置錯誤)
    if count < Test_number: 
        print (f"您輸入的數字{GUESS_string}是{a}A{b}B")
        #利用f-string輸出現有的幾A幾B
    if count >= Test_number:
        Test_limits = False
        #猜測次數達到限制次數後則直接終止迴圈的條件
    a = 0 
    b = 0
    #每次回圈執行完畢都將a和b歸零

if GUESS_string != string:
    print(f"很可惜沒有猜對，答案是{string}")
    #最終如果沒有猜對且不執行迴圈，才執行沒猜對的這段
    #並利用f-string公布答案
