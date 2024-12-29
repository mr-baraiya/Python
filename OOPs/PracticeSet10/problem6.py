from random import randint
class Train:
    # self -> slf kai fer no pade
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
    
    def book(slf,fro,to):
        print(f"Ticket is Booked in Train no : {slf.trainNo} from {fro} to {to}")
    
    def getStatus(slf):
        print(f"Train No : {slf.trainNo} is Running on Time.")
    
    def getFare(slf,fro,to):
        print(f"Ticket is Booked in Train no : {slf.trainNo} from {fro} to {to} is {randint(222,5555)}")
    
t = Train(12399)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")