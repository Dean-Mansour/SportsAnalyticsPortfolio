# Dean Mansour 02/15/2026
# NFL 4TH Down Decision maker

# Title of Program
print("NFL 4th Down Decision Maker: ")

recommendation = ""
reason = ""
# User Inputs
yards_to_go = int(input("How many yards to go? "))
yard_line = int(input("What yard line? "))
score_diff = int(input("What is the score difference? "))
quarter = int(input("What quarter is it? "))
minutes = int(input("How many minutes are left? "))

# What is the situation?
in_opponent_territory = yard_line >= 51
fg_range = yard_line >=60
goal_to_go = yard_line >= 90

# Go for it Situations
if yards_to_go <=3 and in_opponent_territory:
    recommendation = "Go for it!"
    reason = "Short Yardage Situation"
elif  quarter == 4 and minutes <= 5 and score_diff < 0:
     recommendation = "Go for it!"
     reason = "Time running out in the game, do not want to give the opponents the ball back"
elif yards_to_go<=4 and goal_to_go:
   recommendation = "Go for it!"
   reason = "On the goal line, need a touchdown"
# Field Goal Situations
elif score_diff <=3 and fg_range:
     recommendation = "Field Goal"
     reason = "We can tie the game or Be winning the game"
elif score_diff < 0 and quarter == 4 and minutes <=10 and fg_range:
     recommendation = "Field Goal"
     reason = "On the goal line, need a touchdown"
# Punt Situations
elif yard_line <= 40 and yards_to_go >= 6:
     recommendation = "Punt"
     reason = "Long yardage situation in own territory"
else:
     recommendation = "Punt"
     reason = "Long yardage situation in own territory"

print("\n--- Situation Summary ---")
print(f"4th & {yards_to_go} at the {yard_line} yard line")
print(f"Score Difference4: {score_diff} pts | Q{quarter} {minutes}:00")
print("\nRecommedation:", recommendation)
print("Reason:", reason)