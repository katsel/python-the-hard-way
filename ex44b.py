class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

mom = Parent()
daughter = Child()

mom.override()
daughter.override()
