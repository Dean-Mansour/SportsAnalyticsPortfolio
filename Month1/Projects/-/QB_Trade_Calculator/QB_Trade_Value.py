# Using only recent performance (last 3 games), age, and contract cost, determine:
# Which quarterback provides more overall value
# Whether roster constraints change that conclusion
# Whether the trade is clearly favorable or too close to call

# Players being evaluated:
player_names = ["Mathew Stafford", "Jared Goff", "Dak Prescott", "Drake Maye"]
# Same index as player name = same player
# Age of each player:
age = [37, 31, 32, 22]
# Contract Tier:
# (1 = rookie/cheap, 2 = mid, 3 = expensive veteran)
contract_tier = [3, 3, 3, 1]
# Passing yards (last 3 regular season games)
passing_yards = [[245, 298, 196], [225, 334, 202], [188, 361, 251], [287, 230, 268]]
passing_tds = [[1, 2, 2], [1, 5, 1], [0, 2, 1], [1, 2, 2]]
interceptions = [[0, 1, 1], [1, 0, 0], [0, 1, 2], [1, 0, 1]]
sacks = [[3, 1, 1], [4, 0 ,0], [0, 3, 2], [4, 3, 5]]

# Jersey # of the QBs
qbs = [9, 16, 4, 10]
# Menu for the user
print("Choose two QBs by number:")
print("9  — Matthew Stafford (Rams)")
print("16 — Jared Goff (Lions)")
print("4  — Dak Prescott (Cowboys)")
print("10 — Drake Maye (Patriots)")


qb_a = int(input("Enter QB A number: "))
qb_b = int(input("Enter QB B number: "))

# Validation
if qb_a not in qbs or qb_b not in qbs:
    print("Invalid selection: choose a valid QB number from the list.")

elif qb_a == qb_b:
    print("Invalid selection: cannot choose the same QB twice.")

else:
    # Convert QB number -> list index (0–3)
    index_a = qbs.index(qb_a)
    index_b = qbs.index(qb_b)

    print("Valid selection.")
   

 # Their last 3 games performance averages
# QB A:
avg_yds_a = (passing_yards[index_a][0] + passing_yards[index_a][1] + passing_yards[index_a][2]) / 3
avg_td_a  = (passing_tds[index_a][0]   + passing_tds[index_a][1]   + passing_tds[index_a][2])   / 3
avg_int_a = (interceptions[index_a][0] + interceptions[index_a][1] + interceptions[index_a][2]) / 3
avg_sack_a= (sacks[index_a][0]         + sacks[index_a][1]         + sacks[index_a][2])         / 3
print("QB A:", player_names[index_a])
print("QB A avg pass yards:", avg_yds_a)
print("QB A avg TD:", avg_td_a)
print("QB A avg INT:", avg_int_a)
print("QB A avg sacks:", avg_sack_a)
# QB B:
avg_yds_b = (passing_yards[index_b][0] + passing_yards[index_b][1] + passing_yards[index_b][2]) / 3
avg_td_b  = (passing_tds[index_b][0]   + passing_tds[index_b][1]   + passing_tds[index_b][2])   / 3
avg_int_b = (interceptions[index_b][0] + interceptions[index_b][1] + interceptions[index_b][2]) / 3
avg_sack_b= (sacks[index_b][0]         + sacks[index_b][1]         + sacks[index_b][2])         / 3
print("QB B:", player_names[index_b])
print("QB B avg pass yards:", avg_yds_b)
print("QB B avg TD:", avg_td_b)
print("QB B avg INT:", avg_int_b)
print("QB B avg sacks:", avg_sack_b)