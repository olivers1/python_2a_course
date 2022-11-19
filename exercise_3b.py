

class Friend:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    
dict_of_friends = { ("Awesome", "Person"): [
    Friend("Awesome", "Person", "+46709820199"),
    Friend("Awesome", "Person", "+46767670680")
    ],
    ("Bad", "Pal"): [
        Friend("Bad", "Pal", "+46551500400"),
        Friend("Bad", "Pal", "+46100000222")
    ]}

def remove_friend(first, last):
    if (first, last) in dict_of_friends:
        dict_of_friends.pop(first, last)
        print(f"{first}, {last} successfully deleted")

remove_friend("Bad", "Pal")