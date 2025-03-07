class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    information = input().split()

    if information[0] == "Stop":
        break

    current_sender = information[0]
    current_receiver = information[1]
    current_content = information[2]
    email = Email(current_sender, current_receiver, current_content)

    emails.append(email)

send_emails = list(map(int, input().split(", ")))

for index in send_emails:
    emails[index].send()

for current_email in emails:
    print(current_email.get_info())