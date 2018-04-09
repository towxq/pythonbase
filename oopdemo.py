# -*- coding: utf-8 -*-
__author__ = 'wxq'

class A:
    #构造器
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def aaa(self):
        print("A de def aaa")

    def bbb(self):
        print("A de def bbb")

class B:
     #构造器
     def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

     def aaa(self):
        print("B de def aaa")

     def bbb(self):
        print("B de def bbb")

class C(A,B):
    ddd = 12344
    #静态数据
    def ccc(self):
        print ("C de def ccc")


if __name__ ==  '__main__':
    cc = C("wxwq","26")
    print(cc.name+"---"+str(cc.age))
    # cc.aaa()
    cc.ddd = 243123
    print(cc.ddd)
    print(C.ddd)


# python的实例属性可以在实例的创建后的任意时间进行，构造器__init__是设置这些属性的关键点之一，这点和Java的区别，Java必须要提前申明
# 构造器是最早可以设置属性的地方，因为init是实例创建后第一个调用的方法，init执行完毕，即完成了实例化过程

# 类C在创建时，带有一个ddd属性，C.ddd可以访问，当实例cc创建后，对于实例cc而言，访问cc.ddd会失败，但是Python在实例中搜索名字ddd，然后是类，继承树中的基类，然后就找到了
# 我们只有用C.ddd跟新后才能更新他的值，但是实例ccc.ddd中设定时会创建一个实例属性ddd，这样实例是无法访问到C.ddd的，所以实例访问类属性要谨慎 可以del cc.ddd就可以访问类属性了
# 类属性可变的情况是可以的，所以类属性需要修改时，不要使用实例属性来修改

# 方法只有在所属的类有实例时才能被调用，所以任何一个方法的第一个参数就是self，它表示调用该方法的实例对象，其他的对象语言中，self可以称为this



class TestStaticMethod:
    @staticmethod
    def foo():
        print "静态方法"

class TestClassMethod:
    @classmethod
    def foo(cls):
        print "类方法"

# 通常的方法需要一个实例（self）作为第一个参数，对于类方法而言，需要类而不是实例作为第一个参数，类似self,不过很多人使用cls作为变量名字


class P(object):
    def __init__(self):
        print "p's constructor"

class C(P):
    def __init__(self):
        P.__init__(self)  #调用父类的init
        # super(C, self).__init__()  不需要明确父类的名字  当继承的关系改变时，代码不需要做修改
        print "C's constructor"

if __name__ == "__main__":
    c = C()

# 当从一个带构造器init的类继承，如果你不去覆盖init，他将会被继承自动调用，但如果你在子类中覆盖了init，子类实例化时，父类的init不会被自动调用。
# 如果你想调用父类的init需要使用子类的实例去调用父类的方法


# 经典类 类的使用解释的顺序，深度优先，从左到右
class P1:
    def foo(self):
        print "p1 de foo"

class P2:
    def foo(self):
        print "P2 de foo"
    def bar(self):
        print "P2 de bar"

class C1(P1,P2):
    pass

class C2(P1,P2):
    def bar(self):
        print "C2 de bar"

class GC(C1,C2):
    pass

if __name__ == "__main__":
    gc = GC()
    gc.foo()
    gc.bar()

# 新式类 广度优先
class P1(object):
    def foo(self):
        print "p1 de foo"

class P2(object):
    def foo(self):
        print "P2 de foo"
    def bar(self):
        print "P2 de bar"

class C1(P1,P2):
    pass

class C2(P1,P2):
    def bar(self):
        print "C2 de bar"

class GC(C1,C2):
    pass

if __name__ == "__main__":
    gc = GC()
    gc.foo()
    gc.bar()

# Python 2.x中默认都是经典类，只有显式继承了object才是新式类
# Python 3.x中默认都是新式类，不必显式的继承object


# 默认情况下，属性在python中都是公开的，类所在的模块和导入了类所在的其他模块的代码都可以访问到，给数据加上一些可见性，只提供访问函数来访问其值，这就是熟知的隐藏

class PP:
    def __init__(self):
        self.__name = "wxq1213123"#变量私有化

    def __foo(self):
        print "private foo run"

    def getName(self):  # 向外暴露方法
        return self.__name

    def setName(self, newname):
        self.__name = newname

    @property
    def name(self):   # 可以获取私有属性值
        return self.__name

if __name__ == "__main__":
    obj = PP()
    obj.setName("wxqwxq123")
    print obj.getName()
    print obj.name