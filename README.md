# The_Guess_Number_Game  
這是一個猜數字(1A2B)的遊戲  
This is a guessing number game.  
  
編輯環境是使用Visual Studio Code  
程式編譯使用VS code及Python語言  
需要先安裝Python  
其中有使用到numpy模組，請在使用前pip install numpy  
Editor is Visual Studio Code.  
Please install Python first.  
The code include numpy.  
Please 'pip install numpy' in your terminal before you use this code.  
  
#遊戲規則  
輸入4位數字(數字不重複)並按下ENTER  
如果數字及位置正確會回傳A  
如果數字正確但位置錯誤則回傳B  
例：  
題目為1234,當使用者輸入1345  
其中1位置是正確，而3,4雖然是題目數字但位置錯誤，則得到1A2B  
藉由回傳的_A_B數量來推測正確數字  
目前設定猜測次數上限為八次  
若最終沒有猜對會公布正確答案  
  
#GAME_RULE  
Input a four-digit nonrepeating number and put down ENTER.  
If your number is the right digit, it will return "A".  
If your number is the wrong digit, it will return "B".  
Example:
The problem is "1234",and user-input is "1345".  
'1' is the right digits,  and '3','4' is in the problem but thery are wrong digits,  
so the code will return '1A2B'.  
Depending on the return, you can guess the right number.  
You can guess 8 times.  
If user don't guess the right number in 8 times, it will tell you the answer.
