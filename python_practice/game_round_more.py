'''
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''

def game():

    # 变量初始化
    my_hp = my_power = your_hp = your_power = None

    # 进入设置模式，初始血量和战斗力，由用户输入自定义
    while True:
        try:
            my_hp = int(input("input my hp original value:"))
            my_power = int(input("input my power value:"))
            your_hp = int(input("input your original value:"))
            your_power = int(input("input your power value:"))

        #特殊字符捕捉异常
        except ValueError:
            print("Input positive int number please")

        #如果输入的值都是正整数，那么设置成功，退出设置模式
        finally:
            if type(my_hp) == type(my_power) == type(your_hp) == type(your_power) == int:
                if (my_hp > 0 and my_power > 0 and your_hp > 0 and your_power > 0) == True:
                    print("Set value success, go to game round!")
                    break
                else:
                    print("Set value failed, it's supposed to be positive int value, try again!\n")
                    continue
            else:
                print("Set value failed, it's supposed to be positive int value, try again!\n")
                continue

    # if type(my_hp) != int or type(my_power) != int:
    #     raise Exception("please input a int number")

    #开始游戏循环，直到双方中的一方血量为负
    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        print("my_current_hp:" + str(my_hp))
        print("your_current_hp:" + str(your_hp))

        if my_hp <= 0 :
            break
        elif your_hp <= 0 :
            break


    #增加一个判断，比较大小，胜出的一方必然血量更高。这是为了处理该情况：双方血量都即将为负，所以增加此判断条件不然会陷入死循环
    if my_hp < your_hp:
        print("I lost, you win, game over")
    elif my_hp > your_hp:
        print("I win, you lost, game over")
    else:
        print("It's a tie, game over")

game()

