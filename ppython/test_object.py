"""
对象：类
成员方法：类中的一个接口、函数等
成员变量：类中定义的变量
实例化对象：
实例变量： 实例化对象.变量

类方法和实例方法的区别：
1）类方法：不能直接通过【类.方法名】来调用，因为缺少self，需要在方法上加上装饰器@classmethod则可以访问
2）实例方法：可以通过【实例.方法名】
"""

class Person():
    name = 'default'
    age = 10
    tizhong = 0

    @classmethod
    def eat(self):
        print(f"{self.name} eating")


    def jmper(self):
        print(f"{self.age} jumper")


if __name__ == "__main__":
    # 类的实例化
    zs = Person()
    # 实例变量
    print(f"实例变量默认值：{zs.name}")
    zs.name = "张桑"
    print(f"修改实例变量值：{zs.name}")
    # 成员变量（类变量）
    print(f"类变量默认值：{Person.name}")
    Person.name = "李四"
    print(f"类变量修改后：{Person.name}")
    #方法
    Person.eat()
    zs.eat()

