import csv

path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/traningsapp/programmering_test - Blad1.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)

data = []
for row in reader:
    sets = row[0]
    benchpress_reps = float(row[1])
    squat_reps = float(row[2])
    deadlift_reps = float(row[3])
    milpress_reps = float(row[4])

data.append([sets])
data.append([benchpress_reps])
data.append([squat_reps])
data.append([deadlift_reps])
data.append([milpress_reps])
print(data)
print(data[0])

returns_path = "/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/traningsapp/Test_programmering.csv"
file = open(returns_path, "w")
writer = csv.writer(file)
writer.writerow(["sets", "benchpress reps", "squat reps", "deadlift reps", "military press reps"])
writer.writerow(["4x8", 70, 100, 155, 40])