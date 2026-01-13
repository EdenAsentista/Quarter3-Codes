names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = [sum(row) for row in steps]

print("Totals:", totals)
print("Highest:", names[totals.index(max(totals))])
print("Difference:", max(totals) - min(totals))
