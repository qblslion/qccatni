'''
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。

-- by celia 2020.08.09
'''

class Country:
    #  用__slots__ 限制实例的属性,只允许对country实例添加如下的属性
    __slots__ = ("country","name","consistent","language","city")

    #  构造函数自动调用，传入country值
    def __init__(self, country):
        self.country = country
        print(f"Human beings live on the earth, here describes country : {country}")

    def test(self):
        pass

    def Fname(self, name):
        self.name = name
        if name == 'China':
            print(f"{self.country}'s authority name is :the People's Republic of China")
        else:
            print(f"{self.country}'s authority name is :{name}")

    def where(self, consistent):
        self.consistent = consistent
        print(f"{self.country} belongs to {consistent}")


    def speak(self, language):
        self.language = language
        print(f"People in {self.country} speak {language}")

    def capital(self, city):
        self.city = city
        print(f"{self.country}'s capital is {city}")


China = Country('China')
China.Fname("China")
China.where('Aisa')
China.speak('Chinese')
China.capital("Beijing\n")


US = Country("US")
US.Fname("United States of America")
US.where('North America')
US.speak('English')
US.capital("Washington\n")


UK = Country("UK")
UK.Fname("The United Kingdom of Great Britain and Northern Ireland")
UK.where('Europe')
UK.speak("English")
UK.capital("London\n")


Russia = Country("Russia")
Russia.Fname("Russian Federation")
Russia.where("Europe")
Russia.speak("Russian")
Russia.capital("Moscow\n")


Germany = Country("Germany")
Germany.Fname("The Federal Republic of Germany or Moral Country")
Germany.where("Europe")
Germany.speak("German")
Germany.capital("Berlin\n")
