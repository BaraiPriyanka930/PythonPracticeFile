import time
a = input("Enter Your Name:  ")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

h = int(time.strftime("%H"))
if (h<12):
    print("Good Morning", a)
    print("May today be filled with joy, love and happiness")
    
elif (h<17):
    print("Good Afternoon",a)
    print("May your afternoon be as bright and beautiful as you are")
    
else:
    print("Good Evening", a)
    print("May the evening bring you calm, and the night bring the peace ")
    
