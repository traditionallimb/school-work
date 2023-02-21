from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("Ballroom")
ballroom.set_description("A large room with ornate golden decorations on each wall")

diningHall = Room("Dining Hall")
diningHall.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

kitchen.link_room(diningHall, "south")
diningHall.link_room(kitchen, "north")
diningHall.link_room(ballroom, "west")
ballroom.link_room(diningHall, "east")

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)