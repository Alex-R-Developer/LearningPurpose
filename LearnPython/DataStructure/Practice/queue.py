from collections import deque

class CustomerComplaint:
    def __init__(self, name, email, content):
        self.name = name
        self.email = email
        self.content = content

class CustomerServiceCenter:
    def __init__(self):
        self.queue = deque()

    def process_complaint(self):
        if self.queue:

            complaint = self.queue.popleft()
            print(f"{complaint.name}, your {complaint.content} inquiry has been received. We will contact you at {complaint.email} once a representative has been assigned!")
        else:
            print("There are no more inquiries in queue!")

    def add_complaint(self, name, email, content):
        new_complaint = CustomerComplaint(name, email, content)
        self.queue.append(new_complaint)