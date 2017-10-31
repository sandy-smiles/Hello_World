monster_dead = False
has_sword = False
room = 1
end = False


print('The Dark Tunnel')

while not end:
  # start room

  if room == 1:

    print("You are standing at the entrance to a long tunnel.")

    if monster_dead == False:

      print("You hear a low rumble in the distance.")

    print("Actions available: look, forward")
    cmd = input("> ")

    if cmd == 'look':

      if has_sword:

        print("You look around in the darkness, but there is nothing here.")

      else:
        print("You look around in the darkness, and see something shiny.")

        print("It is a sword. Would you like to pick it up (yes/no)? ")

        get = input('> ')

        if get == 'yes':

          print('You pick up the sword.')

          has_sword = True

        else:

          print('You leave the sword in the dust.')

    elif cmd == 'forward':

      room = 2


  # monster room

  elif room == 2:

    if not monster_dead:

      print("When you enter the room, a monster jumps out at you,")

      print("its fangs white and sharp in the darkness.")

      if has_sword:

        print("You draw your sword and thrust it towards the leaping body.")

        print("Your strike hits true and kills the monster.")

        monster_dead = True

        has_sword = False

      else:

        print("With no way of defending yourself, the monster crushes")

        print("your body and sinks its teeth into your flesh.")

        print("You are dead.")

        print("Game Over.")

        end = True

    elif not has_sword:

      print("The monster's dead carcass lies on the floor,")

      print("the sword still embedded in its flesh.")

      print("Would you like to pick up the sword(yes/no)? ")

      get = input('> ')

      if get == 'yes':

        print('You pull out the sword from the monster.')

        has_sword = True

      else:

        print('You leave the sword in the monster.')

    else:

      print("The monster's dead carcass lies on the floor,")

      print("There is a hole in its flesh.")



    # if the player is still alive, they can move

    if not end:

      print("Actions available: forward, backward, look")

      cmd = input("> ")

      if cmd == 'forward':

        room = 3

      elif cmd == 'backward':

        room = 1

      elif cmd == 'look':

        room = 2



  # exit - win condition

  else:

    print("You made it past the monster and have escaped the tunnel.")

    print("Congratulations, you win.")

    end = True
