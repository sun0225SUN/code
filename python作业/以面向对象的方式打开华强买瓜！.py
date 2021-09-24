class Person:
    def __init__(self, name):
        self.name = name


class LiuHUaQiang(Person):
    def __init__(self, name):
        self.name = name

    def buy_watermelon(self):
        print(self.name + "开口询问：" + "哥们儿，你这瓜多少钱一斤哇？")

    def say_expensive(self):
        print(self.name + "微微一笑：" + "what's up，这瓜皮子是金子做的，还是瓜粒子是金子做的?")

    def bug_one(self):
        print(self.name + "：" + "行，给我挑一个！")

    def doubt(self):
        print(self.name + "：" + "你这瓜保熟么？")

    def find_cha(self):
        print(self.name + "：" + "我问你这瓜保熟吗?")

    def is_shou(self):
        print(self.name + "：" + "你这瓜要是熟我肯定要哇！")

    def not_shou(self):
        print(self.name + "：" + "那它要是不熟怎么办！")

    def doubt_not(self):
        print(self.name + "：" + "眉头一皱：" + "你这哪够十五斤啊？，你这称有问题啊！")

    def found_cha(self):
        print(self.name + "：" + "把秤盘子翻了过来：" + "吸铁石，另外你说的，这瓜要是生的，你自己吞进去啊。")


class Boss():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name + "正在和小弟们叨叨: " + "生异性吗，哥几个？")

    def sell_watermelon(self):
        print(self.name + "：" + "两块钱一斤！")

    def say_dapeng(self):
        print(self.name + "：" + "你瞧瞧这现在哪有瓜呀?这都是大棚的瓜，你嫌贵我还嫌贵呢。")

    def say_howthisone(self):
        print(self.name + "拿起一个瓜，问：" + "这个怎么样？")

    def sell_shenggua(self):
        print(self.name + "：" + "我开水果摊儿的，能卖给你生瓜蛋子啊?")

    def find_cha(self):
        print(self.name + "直起身子怒目而视地问到：" + "你是故意找猹儿是不是?你要不要吧!")

    def boss_eat(self):
        print(self.name + "：" + "哎，要是不熟，我自己吃了它，满意了吧?")

    def weigh_watermelon(self):
        print(self.name + "15斤，30块。")

    def pwg(self):
        print(self.name + "你特么劈我瓜是吧，我……")


class Litter_brother(Person):
    def __init__(self, name):
        self.name = name

    def shouting(self):
        print(self.name + "说: " + "萨日朗!萨日朗")


class Frind(Person):
    def __init__(self, name):
        self.name = name

    def find_huaqiang(self):
        print(self.name + "说: " + "华强，哎，华强!")


class Aside(Person):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    # 实例化类，创建对象
    liuhuaqiang = LiuHUaQiang("刘华强")
    boss = Boss("水果摊老板")
    litter_brother = Litter_brother("小弟")
    friend = Frind("华强朋友")
    aside = Aside("旁白")

    # 正文，开始调用对象和方法，满足业务逻辑
    print()
    print("有一个人前来买瓜")
    print(liuhuaqiang.name + "骑着摩托，从树边写着“香草莓特甜5元2斤”的招牌经过，来到水果摊前。")
    boss.talk()
    liuhuaqiang.buy_watermelon()
    boss.sell_watermelon()
    liuhuaqiang.say_expensive()
    boss.say_dapeng()
    liuhuaqiang.bug_one()
    print("水果摊老板转身挑瓜")
    print("拍瓜声咚咚咚，摊主在试图安抚西瓜的情绪。")
    boss.say_howthisone()
    liuhuaqiang.doubt()
    boss.sell_shenggua()
    liuhuaqiang.find_cha()
    boss.find_cha()
    liuhuaqiang.is_shou()
    boss.boss_eat()
    boss.weigh_watermelon()
    liuhuaqiang.doubt_not()
    liuhuaqiang.found_cha()
    print("说完之后" + liuhuaqiang.name + "一刀把西瓜劈开，劈出了一个0.618的黄金比例。")
    boss.pwg()
    print("水果摊主冲了上去，刘华强用手一挡他的胳膊，一刀剖在了他的肚子上。")
    litter_brother.shouting()
    print("水果摊主的小弟边喊边拿着武器冲向" + liuhuaqiang.name + liuhuaqiang.name + "冷静地用刀指着他。")
    print("路边的一家三口出现在了画面里，穿西装的男人认出了昔日的旧友华强")
    friend.find_huaqiang()
    print("刘华强骑着摩托，转过头，邪魅一笑，便扬长而去。。。")
