command=""
started= False
while True:
    command= input("> ").lower()
    if command == "start":
        if started:
            print("CAr is already started")
        else:
            started= True
        print(f'The car has started...')
    elif command== "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started= False
        print(f'the car has stopped...')
    elif command =="help":
        print("""
start- to start the car
stop- to stop the car
quit- to exit
        """)
    elif command=="quit":
        break
    else:
        print("I dont't understand this")