# wap to create a class named distance which has feet and inches as data member, overload any two operators
# download numpy, scikit-learn pandas, streamlit matplotlib.pyplot
class Distance:

    def __init__(self, feet, inches):
        self.f = feet
        self.i = inches

        
    def __str__(self):
        return f"({self.f}, {self.i})"
    
    def __add__(self, other):
        new_feets = self.f + other.f
        new_inches = self.i + other.i
        return Distance(new_feets, new_inches)
    

        

