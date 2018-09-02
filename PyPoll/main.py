import os
import csv
import pandas as pd
import numpy as np

open_poll_csv = os.path.join("Resources", "election_data.csv")

output_poll_csv = os.path.join("Output", "poll_result.csv")

vote_count = 0
            
vote_count = len(open(open_poll_csv, newline='').readlines())-1

poll_df = pd.read_csv(open_poll_csv)

list_candidate = poll_df["Candidate"].unique()

vote_count_by_cand = poll_df["Candidate"].value_counts(ascending = False)

list_votes= [str("{:.2f}%".format(100*vote_count_by_cand[i]/vote_count)) + " (" + str(vote_count_by_cand[i]) +")"
 for i in range(0,len(vote_count_by_cand)) ]

print("Election results")

print("-----------------------------------\n")

print(f"Total Votes: {vote_count}") 

print("-----------------------------------\n")

# result = pd.DataFrame(np.column_stack([list_candidate, list_votes]),
# columns = ['Candidate','Vote% (population)']
# )

# print(result.to_string(index=False))

results = list(zip(list_candidate, list_votes))
print( "\n".join([f"{result[0]}: {result[1]}" for result in results]) )

print("-----------------------------------\n")

winner = results[0][0]
print(f"Winner is {winner} ")


with open(output_poll_csv,"w", newline="") as outputfile:        
    csvwriter = csv.writer(outputfile, lineterminator='\n')

    csvwriter.writerow(["Election results"])
    
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow([f"Total Votes: {vote_count}"])

    csvwriter.writerow(["---------------------------"])
    for result in results:
        csvwriter.writerow([f"{result[0]}: {result[1]}"])
    
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow([f"Winner is {winner}"])




