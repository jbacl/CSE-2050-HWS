class Task:
    def __init__(self,id,time_left):
        self.id=id
        self.time_left=time_left
        self.next=None
        self.prev=None
    
    def reduce_time(self,time_amount):
        self.time_left=self.time_left - time_amount
    
    def __str__(self):
        return "ID: "+str(self.id)+" Time left: "+str(self.time_left)
