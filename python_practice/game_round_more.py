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
    # my_hp = 1000
    # my_power = 200
    # your_hp = 1000
    # your_power = 199

    my_hp = my_power = your_hp = your_power = None

    while True:
        try:
            my_hp = int(input("input my hp original value:"))
            my_power = int(input("input my power value:"))
            your_hp = int(input("input your original value:"))
            your_power = int(input("input your power value:"))

        except ValueError:
            print("Input positive int number please")
        finally:
            if type(my_hp) == type(my_power) == type(your_hp) == type(your_power) == int:
                print((my_hp > 0)==True)
                print((my_power > 0) == True)
                print((your_hp > 0) == True)
                print((your_power > 0) == True)
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

    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        print("my_current_hp:" + str(my_hp))
        print("your_current_hp:" + str(your_hp))

        if my_hp <= 0 :
            break
        elif your_hp <= 0 :
            break

    if my_hp < your_hp:
        print("I lost, you win, game over")
    elif my_hp > your_hp:
        print("I win, you lost, game over")
    else:
        print("It's a tie, game over")

game()

