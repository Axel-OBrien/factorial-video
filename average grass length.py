# https://bioadvanced.com/how-high-mow-your-lawn

ranges = [
    "0.5-3",
    "0.75-3.5",
    "0.75-2.5",
    "1.5-4",
    "0.5-2.5",
    "1.5-4",
    "1-1.5",
    "1.0-3.0",
    "0.5-2",
]

averages = list(map(lambda x: 
    (float(x.split("-")[0]) + float(x.split("-")[1])) / 2,
ranges))

sum_of_averages = sum(averages) / len(averages)
print(sum_of_averages)