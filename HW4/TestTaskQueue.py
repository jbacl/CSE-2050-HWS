class TaskQueue:
    def __init__(self,time_per_task=1):
        self.current=None
        self.len=0
        self.time_per_task=time_per_task
        
    def is_empty(self):
        return self.current==None
    
    def add_task(self,task):
        if self.is_empty():
            task.next=task
            task.prev=task
            self.current=task
            self.len=self.len+1
            return
        
        
        task.prev=self.current.prev
        task.next=self.current
        
        self.current.prev.next=task
        self.current.prev=task
        
        self.current=task
        self.len=self.len+1
        
    def remove_task(self,id):
        if self.is_empty():
            print("Runtime error: id "+str(id)+" not in TaskQueue")
            return
        
        temp1=self.current
        temp2=self.current
        while True:
            if temp2.id==id:
                #only one node
                self.len=self.len-1
                if temp2.next==temp2:
                    self.current=None
                    return
                #task to be deleted is the current task
                if temp2==self.current:
                    self.current=temp2.next
                    
                temp2.next.prev=temp2.prev
                temp2.prev.next=temp2.next
                return
            
            temp2=temp2.next
            
            if temp1==temp2:
                break
        print("Runtime error: id "+str(id)+" not in TaskQueue")
    
    def execute_tasks(self):
        time=0
        while True:
            if self.is_empty():
                break
            temp=self.current
            if temp.time_left<=self.time_per_task:
                temp.reduce_time(temp.time_left)
            else:
                temp.reduce_time(self.time_per_task)
            
            if temp.time_left==0:
                self.remove_task(temp.id)
                print(" Finished task "+str(temp.id)+" at t = "+str(time)+" seconds")
            
            time=time+1
        
        return time
