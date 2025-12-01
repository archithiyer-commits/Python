print("Hello user! I'm an AI chatbot. What's your name? ")
name = input()

print(f"Nice to meet you, {name}!")

print("How are you feeling today?(Good/Bad)")
mood = input().lower()

if mood == "good":
  print("Im happy!")

elif mood == "bad":
  print("Womp womp")

else:
  print("I see. You cant say what you want to because you're dumb.")


print("Bye bye")