from functions import *
import time
import sys


if __name__ == '__main__':
    """This program can be used to tell your daily future with three coins:-)
    
    Theory at https://www.jianshu.com/p/6fd916cc65a9
    Hexagram data from 易安居 Website at https://www.zhouyi.cc/zhouyi/yijing64/
    
    You just need three coins and this program.
    
    Steps:
    1. Take out three coins. Decide which side is Yin and which is Yang according to personal preference.
    2. Find a quiet place and wash your hands first with a decent attitude:-)
    3. Hold three coins in the palm of your hand with both hands. You must think clearly about what to count!
     Then concentrate your thoughts highly.
    4. Then the hand started to shake. After a few shakes, throw the coins to the ground (or any flat surface).
    5. Type the head result of this throwing into this program and repeat this step for six times.
    6. Done! You can read the explanation of hexagrams in the program.
    """

    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$\t\t\t\t欢迎使用\t\t\t\t $\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
    time.sleep(1)
    print('--------------------------------------\n')
    print('有关程序的说明：\n')
    print('--------------------------------------\n')
    print('这是一个硬币起卦和解卦的小程序:-)你需要三枚相同规格的硬币和一个健全的大脑，并保证本程序可以连接上网络:-)。\n')
    print('起卦（掷硬币）环节需要默念要算的东西并态度端正、意念集中。当然，你能斋戒沐浴顺便焚个香更好（划掉&笑\n')
    print('程序原理在 https://www.jianshu.com/p/6fd916cc65a9 中可以找到。\n')
    print('程序源码在 https://github.com/usernameAlreadyTaken7Times/Coin_Future_Telling 中可以找到。\n')
    print('程序解卦数据采用了易安居网站 https://www.zhouyi.cc/zhouyi/yijing64/ 的数据。\n')
    time.sleep(2)
    print('--------------------------------------\n')
    print('下面让我们愉快地开始吧！硬币就位？脑子还在？那么，____, 启洞！\n')
    print('**************************************\n\n')

    error_time = 0
    input_list = []

    for num_time in range(1, 7):
        num, error_time = get_input(num_time, error_time)
        input_list.append(num)

    # confirm the input
    print(f'确认一下，你的六次掷硬币正面的数量分别为{str(input_list)}。')
    print('--------------------------------------\n')
    time.sleep(2)

    print('**************************************\n\n')

    # retrieve the hexagram result
    hex_result = set_hex(input_list)

    # get the explanation of the hexagram
    result_text = get_instructions(hex_result[0], hex_result[1], hex_result[2])

    # output the result text
    print(result_text)

    sys.exit()
