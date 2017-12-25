import matplotlib.pyplot as plt

fig, axes = plt.subplots(3,3)
for i in range(3):
    for j in range(3):
        ax = axes[i, j]
        if i == 0:
            title = ax.set_title("column title", loc = 'center', y = 1.1)
        if j == 2:
            text = ax.text(1.1, 0.5, "row title", size = 12,
                           verticalalignment = 'center', rotation = 270)

plt.savefig('Columns_and_row_titles.png')
plt.show()