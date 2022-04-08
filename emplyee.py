class Employee():

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.payment = ''
        
    def give_raise(self, aumento):
        aumento = 5000
        self.payment.append(aumento)
        