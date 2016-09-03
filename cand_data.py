import csv
from collections import defaultdict
import sys
 
def main(input_file_name, city):
    csv_reader = csv.reader(open(input_file_name))
    
    header = csv_reader.next()
    
    for i in xrange(len(header)):
        field = header[i]
    
        if field == 'PRECINCT_NAME':
            PRECINCT = i 
        if field == 'CANDIDATE_FULL_NAME':
            CAND_NAME = i 
        if field == 'TOTAL':
            TOTAL = i 
    
    precinct_totals = defaultdict(int)
    cand_totals = {}
    
    for line in csv_reader:
        precinct_name = line[PRECINCT]
        cand_name = line[CAND_NAME]
        total = float(line[TOTAL])
        
        precinct_totals[precinct_name] += total
        if cand_name not in cand_totals:
            cand_totals[cand_name] = defaultdict(int)
        cand_totals[cand_name][precinct_name] += total

    cand_names = sorted(cand_totals.keys())
    precincts = sorted(cand_totals[cand_names[0]].keys())

    cand_txt = open('{}_data.txt'.format(city), 'w')
    cand_csv = open('{}_data.csv'.format(city), 'w')

    # Write CSV header
    cand_csv.write('"","{}"\n'.format('","'.join(precincts)))

    for candidate in cand_names:
        cand_tuples = []
        # Write candidate name in CSV
        cand_csv.write('"{}"'.format(candidate))
        for precinct in precincts:
            cand_percent = cand_totals[candidate][precinct] / precinct_totals[precinct] * 100
            cand_tuples.append((precinct, cand_percent))
            # Write percentages in CSV
            cand_csv.write(',"{}"'.format(cand_percent))
        # Go to CSV newline
        cand_csv.write("\n")
            
        cand_tuples.sort(key=lambda t: t[1])
        
        cand_txt.write(candidate + "\n")
        for tup in cand_tuples:
            cand_txt.write("{}: {:.2f}%\n".format(tup[0], tup[1]))
        cand_txt.write("\n")

    cand_txt.close()
    cand_csv.close()
 
if __name__ == "__main__":
    input_file_name = sys.argv[1]
    city = sys.argv[2]
    main(input_file_name, city)
