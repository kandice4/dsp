# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

with open("football.csv") as football_csv:
    football_list = list(football_csv)

football_data = []
    
for line in football_list:
    w_line = line.split(",")
    w_line[-1] = w_line[-1].strip()
    for i in range(len(w_line)):
        try:
            w_line[i] = int(w_line[i])
        except ValueError:
            pass
    football_data.append(w_line)

football_stat_type = {b:a for (a,b) in enumerate(football_data[0][1:])}
football_teams = {a:b for (a,b) in enumerate([x[0] for x in football_data[1:]])}
football_stats = [x[1:] for x in football_data[1:]]
goal_abs_diff = []
smallest_diff = []

for stat in football_stats:
    goal_abs_diff.append(abs(stat[football_stat_type['Goals']]-stat[football_stat_type['Goals Allowed']]))

for diff in goal_abs_diff:
    if diff == min(goal_abs_diff):
        smallest_diff.append([football_teams[goal_abs_diff.index(diff)],diff])
        
print(smallest_diff)
