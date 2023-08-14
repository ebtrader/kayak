import regex as re
import pandas as pd

with open("costco.txt", "r") as file:
    data = file.read()

sections = re.split(r'Add', data)
prices = []
info1 = []
info2 = []

for section in sections[1:]:
    lines = section.strip().split("\n")
    price = None
    for line in lines:
        if line.startswith("$"):
            match = re.search(r'\$(\d+\.\d{2})', line)
            if match:
                price = float(match.group(1))
                info1.append(lines[lines.index(line) + 1].strip())
                info2.append(lines[lines.index(line) + 2].strip())
                prices.append(price)
            else:
                info1.append(None)
                info2.append(None)
                prices.append(None)

df = pd.DataFrame({
    'Price': prices,
    'Info1': info1,
    'Info2': info2
})

print(df)
