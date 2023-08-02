#TASK 1
student_age = []
school_house = []
reaction_time = []

saturn_count = 0
mars_count = 0
saturn_reaction_time = 0
mars_reaction_time = 0

#TASK 2
for i in range(1, 4):
  print(f"PARTICIPANT {i}'S TURN"
        "\n")
  house_input = input("What house are you in? >>>")
  school_house.append(house_input)

  if house_input == "Saturn" or house_input == "saturn" or house_input == "satrun" or house_input == "Satrun":
    saturn_count += 1
    saturn_reaction_time_input = float(
        input("How long did your reaction take (in seconds)? >>>"))
    reaction_time.append(saturn_reaction_time_input)
    saturn_reaction_time += saturn_reaction_time_input
    avg_saturn_reaction_time = saturn_reaction_time / saturn_count

  elif house_input == "Mars" or house_input == "mars":
    mars_count += 1
    mars_reaction_time_input = float(
        input("How long did your reaction take (in seconds)? >>>"))
    reaction_time.append(mars_reaction_time_input)
    mars_reaction_time += mars_reaction_time_input
    avg_mars_reaction_time = mars_reaction_time / mars_count
  else:
    print("Enter a house between Saturn or Mars.")

  age_input = int(input("How old are you? >>>"))
  if age_input > 16 or age_input < 12:
    print("You must be between 16 and 12 to participate.")
  else:
    student_age.append(age_input)
  print("\n")

reaction_time.sort()
print("\n"
      "The slowest reaction time was", reaction_time[-1])

avg_reaction_time = sum(reaction_time) / len(reaction_time)
print("\n"
      "The average reaction time was", avg_reaction_time)
