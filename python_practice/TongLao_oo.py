'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造

-- by celia  2020.08.09
'''

# reference:
# 经验值：EXP（baiExperience）
# 战斗力：CE（Combat Effectiveness)
# 血量：HP(Health Point）
# 魔力值：duMP(Magic Point)
# 级别/级数：LV(Level)
# 普通金钱：Cash/Money/Game Point(常用zhi图标dao代替)
# 黄金：Gold(常用图标代替)
# 钻石：Diamond(常用图标代替)
# 武器：Weapon
# 主武器：Primary Weapon
# 副武器：Secondary Weapon
# 伤害：Damage
# 杀敌：Kill
# 弹药：AMMO/Ammunition
# 爆头：Head Shot


def if_meet_DCQ(f):
    def battle(a,b,c,d):
        print(f"遇到{b}")
        print("----开始战斗，决一死战----")
        f(a,b,c,d)
        print("----输赢已定，战斗结束----\n")
    return battle


class TongLao:
    hp = 1000
    power = 50
    meet_name = None
    my_name = "童姥"

    def __init__(self):
        pass

    def see_people(self, meet_name):
        self.meet_name = meet_name
        print(f"TongLao sees {self.meet_name}:")
        if meet_name == "WYZ" or meet_name == "无崖子":
            print("师弟！\n")
        elif meet_name == "LQS" or meet_name == "李秋水":
            print("贱人就是矫情\n")
        elif meet_name == "DCQ" or meet_name == "丁春秋":
            print("叛徒，灭了你\n")
        else:
            print("你是哪个庙的和尚？\n")

    @if_meet_DCQ
    def fight_zms(self, name, enemy_hp, enemy_power):
        self.power *= 10
        self.hp /= 2

        # print(f"{self.my_name}VS{name} 战斗开始...")
        after_fight_hp = self.hp - enemy_power
        after_fight_hp_enemy = enemy_hp - self.power

        if after_fight_hp - after_fight_hp_enemy <= 0 :
            print(f"{self.my_name}输了,{name}赢了")
        else:
            print(f"{self.my_name}赢了，{name}输了")

        # print(f"{self.my_name}VS{name} 战斗结束...\n")


class XuZhu(TongLao):
    my_name = "xuzhu"

    def __init__(self):
        print("虚竹：……我佛慈悲，与世无争，不要cue我……")

    def read(self):
        print("虚竹：罪过罪过……\n")


t1 = TongLao()
t1.see_people("WYZ")
t1.see_people("LQS")
t1.see_people("DCS")
t1.see_people("NPC")

xz = XuZhu()
xz.read()

t1.fight_zms("丁春秋",300,100)