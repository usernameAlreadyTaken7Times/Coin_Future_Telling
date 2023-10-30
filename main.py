from functions import *
import time
import os
import sys


def test_input_and_error_manage(input_num, error_num):
    """Use this function to test if the input in the main program is valid, and if not, return the corresponding output.
    """

    type_error = False
    value_error = False
    value_too_big = False

    quit_code = False

    # check weather the input is valid
    try:
        input_num = int(input_num)
    except ValueError:
        type_error = True
        error_num += 1

    if not type_error:
        if 0 <= input_num <= 3:
            pass
        elif input_num > 3:
            value_error = True
            value_too_big = True
            error_num += 1
        else:
            value_error = True
            error_num += 1

    # if not valid, give out the result
    if type_error:
        if error_num == 1:
            print('亲，请输入数字。')
        elif error_num == 2:
            print('亲，请输入正确的数字可好？0到3！两次了都，别搞啊。')
        elif error_num == 3:
            print('数字！数字！只输入数字，0到3！别输别的！你能行的，相信自己！')
        elif error_num == 4:
            print('.......来，我们各退一步，你认真输数字，我保证不打你（温柔），记得输正确的数字啊，0到3！')
        elif error_num == 5:
            print('最后一次提醒了，真的。输!数!字!0!到!3!我们就还是好朋友（咬牙切齿）。')
        elif error_num == 6:
            print('你完了!地爆天星！')
            time.sleep(2)
            quit_code = True

    if value_error:
        if error_num == 1:
            print('亲，数字不太对。三个硬币掷出的正面应该在0和3之间，你说对吧？')
        elif error_num == 2:
            if value_too_big:
                print(f'我认为，三个硬币是无论如何都掷不出{str(input_num)}个正面的。要不再来一次？')
            else:
                print(f'我认为，三个硬币是无论如何都掷不出{str(input_num)}个正面的。要不再来一次？')
        elif error_num == 3:
            print('我从未设想过输入0到3的数字竟如此困难，真的。')
        elif error_num == 4:
            print('.......来，我们各退一步，你认真输数字，我保证不打你（温柔），记得输正确的数字啊，0到3！')
        elif error_num == 5:
            print(f'最后一次提醒了，真的。输!数!字!0!到!3!三个硬币到底要怎么做才能掷出{str(input_num)}个正面啊！（咬牙切齿）')
        elif error_num == 6:
            print('你完了!地爆天星！')
            time.sleep(2)
            quit_code = True

    if type_error or value_error:  # there is an error with the input
        return False, error_num, quit_code
    else:
        return True, error_num, quit_code


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
    num_1 = -1
    num_2 = -1
    num_3 = -1
    num_4 = -1
    num_5 = -1
    num_6 = -1

    num_1_valid = False
    while not num_1_valid:
        num_1 = input('来，默念你要算的东西，然后掷一次硬币，并输入正面的数量：')
        num_1_valid, error_time, quit_code = test_input_and_error_manage(num_1, error_time)
        if quit_code:
            print('好吧你完了，但又没完全完。这次只是注销系统，下次就直接关你机了！')  # actually not:-)
            os.system('RunDll32.exe user32.dll, LockWorkStation')
            time.sleep(5)
            sys.exit(0)
    num_1 = int(num_1)

    num_2_valid = False
    while not num_2_valid:
        num_2 = input('继续默念你要算的东西，然后再掷一次硬币，并输入正面的数量：')
        num_2_valid, error_time, quit_code = test_input_and_error_manage(num_2, error_time)
        if quit_code:
            print('好吧你完了，但又没完全完。这次只是注销系统，下次就直接关你机了！')  # actually not:-)
            os.system('RunDll32.exe user32.dll, LockWorkStation')
            time.sleep(5)
            sys.exit(0)
    num_2 = int(num_2)

    num_3_valid = False
    while not num_3_valid:
        num_3 = input('再来一次，输入正面的数量：')
        num_3_valid, error_time, quit_code = test_input_and_error_manage(num_3, error_time)
        if quit_code:
            print('好吧你完了，但又没完全完。这次只是注销系统，下次就直接关你机了！')  # actually not:-)
            os.system('RunDll32.exe user32.dll, LockWorkStation')
            time.sleep(5)
            sys.exit(0)
    num_3 = int(num_3)

    num_4_valid = False
    while not num_4_valid:
        num_4 = input('第四次正面的数量：')
        num_4_valid, error_time, quit_code = test_input_and_error_manage(num_4, error_time)
        if quit_code:
            print('好吧你完了，但又没完全完。这次只是注销系统，下次就直接关你机了！')  # actually not:-)
            os.system('RunDll32.exe user32.dll, LockWorkStation')
            time.sleep(5)
            sys.exit(0)
    num_4 = int(num_4)

    num_5_valid = False
    while not num_5_valid:
        num_5 = input('第五次正面的数量：')
        num_5_valid, error_time, quit_code = test_input_and_error_manage(num_5, error_time)
        if quit_code:
            print('好吧你完了，但又没完全完。这次只是注销系统，下次就直接关你机了！')  # actually not:-)
            os.system('RunDll32.exe user32.dll, LockWorkStation')
            time.sleep(5)
            sys.exit(0)
    num_5 = int(num_5)

    num_6_valid = False
    while not num_6_valid:
        num_6 = input('最后一次正面的数量：')
        num_6_valid, error_time, quit_code = test_input_and_error_manage(num_6, error_time)
        if quit_code:
            print('好吧你完了，但又没完全完。这次只是注销系统，下次就直接关你机了！')  # actually not:-)
            os.system('RunDll32.exe user32.dll, LockWorkStation')
            time.sleep(5)
            sys.exit(0)
    num_6 = int(num_6)

    # confirm
    print(f'确认一下，你的六次掷硬币正面的数量分别为{str([num_1, num_2, num_3, num_4, num_5, num_6])}。')
    print('--------------------------------------\n')
    time.sleep(3)

    print('**************************************\n\n')

    # build a hexagram with the coin results
    num_list = [num_1, num_2, num_3, num_4, num_5, num_6]
    hex_result = set_hex(num_list)

    # get the explanation of the hexagram
    result_text = get_instructions(hex_result[0], hex_result[1], hex_result[2])

    # output the result text
    print(result_text)

    sys.exit()
