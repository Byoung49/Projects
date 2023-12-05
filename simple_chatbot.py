# UNIBUDDY.PY
'''
[Case Study Story] --> Imagine the first day of university for a freshman named Alex. 
Alex is excited but also overwhelmed by the vast campus, numerous courses, and the sea of new faces. 
To aid new students like Alex, the university's IT department has developed a personalised chatbot. 
This chatbot, named "UniBuddy", is designed to make the transition smoother for freshmen.
Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and age. 
Based on this input, UniBuddy offers a personalised greeting.
For instance, if Alex's favourite colour is blue,
    UniBuddy might suggest joining the university's "Blue Art Club".
If Alex is 18, the chatbot might provide information about freshman-specific events.
The chatbot also offers a feature where Alex can input specific queries, like "Where is the library?"
    or "How do I join the debate club?", 
        and UniBuddy responds with relevant information, all while adhering to a friendly tone,
        using string transformation methods to ensure the responses feel personalised and engaging.
'''

# initialise message for first time start
print("""
Welcome to UniBuddy! Your all-in-one app that
makes your freshman journey a bit easier to navigate
      
Please enter your credentials to get started! : """)

user_name = input("Please enter your student name : ").capitalize()
user_age = int(input("Please enter your age : "))
fav_colour = input(
    "Please enter your favorite colour from the options:Red, Blue, Green, Yellow : ").capitalize()

print(f"""
Welcome {user_name}! I see that your favorite colour is {fav_colour}.
I have a few suggestions based on your choice!      
""")

if fav_colour == 'Red':

    print(f"If you like the colour RED {user_name}, I have the following for you! Checkout : ")

    print("""
1. Our red colour themed football club.
2. Our red themed art club.
3. Our red carpet graduation celebration.
4. Our postman Pat event.
""")
elif fav_colour == 'Blue':

    print(f"If you like the colour BLUE {user_name}, I have the following for you! Checkout : ")

    print("""
1. Our blue colour themed swimming club.
2. Our blue themed art club.
3. Our blue smurf event.
4. Our fishing club.
""")
elif fav_colour == 'Green':
    print(f"If you like the colour GREEN {user_name}, I have the following for you! Checkout : ")

    print("""
1. Our Golf society
2. Our climate change club.
3. Our gardening community. 
4. Our sustainable future's council.
""")
elif fav_colour == 'Yellow':
    print(f"If you like the colour YELLOW {user_name}, I have the following for you! Checkout : ")

    print("""
1. Our beach club.
2. Our sand castle building club.
3. Our baking club. 
4. Our yellow flower growing club. 
""")
else:
    (f"The colour you entered has not been recognized from our list {user_name}, please choose again : ")

if user_age <= 22:

    print("Here are some freshman specific events : ")

    print("""
    1. Freshman social club
    2. Freshman study club
    3. Freshman dance club 
    4. Freshman sports club open event
    """)
elif user_age >= 40:
    print("Here are some mature student specific suggestions : ")

    print("""
    1. Why not join our Hiking group?
    2. How about the voluntary groundskeeping club?
    3. Maybe you would find joy in the over 35's social club, thursdays at 16:00
    4. We even have a group bingo!! 
    """)
    
else:
    print(f"{user_name}, here are a few event suggestions you may be interested in! : ")

    print("""
    1. Freshers night(Tuesdays at 6pm until late)
    2. Group study night(All freshers welcome!)
    3. Data visualisation support
    4. Fish Friday at the student bar! (The best fish around!)
    """)

question = input(f"Is there anything else you would like me to help you with {user_name}? (enter Quit to leave this chat) : ")
if question == "Quit":
    print(f"Goodbye {user_name}! Speak with you soon.")

elif question == "where is the library?":
    print("""
    You can find the library directly opposite the food hall, there is a yellow door,
    with some beautiful flowers surrounding the entrance!
    """)
elif question == "how do i join the debate club?":
    print(f"""
    Oh, great question {user_name}! To join the debate club please head to www.yourUni.com and look for the debate club on the navigation bar to 
    the left of the page! 
    """)
    lower(input("If this is everything, please enter Quit to leave the chat : "))
else:
    input(f"I will get back to you on this! If that is everything {user_name} we at UniBuddy hope you have an amazing day!")
