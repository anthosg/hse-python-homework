import pandas as pd
import matplotlib.pyplot as plt

colors = [
    '#FF6F61', '#FFB347', '#FFD700', '#77DD77', '#AEC6CF', 
    '#C39BD3', '#9B59B6', '#6B5B95', '#88B04B', '#FF6F61'
]

data = pd.read_json("events.json")
df = pd.DataFrame(data["events"].tolist())
df["signature"] = df["signature"].str.replace(" ", "\n")

counts = df["signature"].value_counts()
plt.figure(figsize=(20,8))
counts.plot(kind='bar', color=colors)

plt.title("Распределение событий информационной безопасности по их типам")
plt.ylabel("Количество")
plt.xlabel("")
plt.xticks(rotation=0, ha="center")

plt.tight_layout()
plt.show()
