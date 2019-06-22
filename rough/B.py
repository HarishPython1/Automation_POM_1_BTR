from rough.A import A
class B(A):
    def __init__(self,course):
        self.course=course
        print("inside B constr ",self.course)

b=B("selenium")

