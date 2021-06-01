class Scheme:
    scheme_id = 1
    scheme_name = "Jio prepaid"
    outgoing_rate = 1.9
    message_charge = 2.5
    def display(self):
        print("scheme_id: ",self.scheme_id)
        print("scheme_name: ",self.scheme_name)
        print("outgoing_rate: ",self.outgoing_rate)
        print("message_charge: ",self.message_charge)

class Customer(Scheme):
    cust_id = 1
    name = "Devalsinh Zala"
    mobile_no = 5693285153
    def display1(self):
        print("cust_id: ",self.cust_id)
        print("name: ",self.name)
        print("mobile_no: ",self.mobile_no)

cust = Customer()
cust.display()
cust.display1()