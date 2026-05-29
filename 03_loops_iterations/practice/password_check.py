correct_password = "Python123"

for i in range(1, 4):
  print(f"Attempt {i}:")
  password = input("Enter password: ")
  if correct_password == password:
    print("Access Granted!")
    break
  elif password == "skip":
    continue
  print("Wrong Password. Try again.")
else:
  print("System Locked")