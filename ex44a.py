class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

mom = Parent()
daughter = Child()

mom.implicit()
daughter.implicit()
