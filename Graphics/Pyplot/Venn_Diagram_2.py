import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
from matplotlib_venn import venn3, venn3_circles

## ========== ##
## EXAMPLE  1 ##
## ========== ##

figure, axes = plt.subplots(2, 2)

# 1:
venn2(subsets = {'10': 1, '01': 1, '11': 1}, set_labels = ('A', 'B'), ax = axes[0][0])
# 2:
venn2_circles((1, 2, 3), ax = axes[0][1])
# 3:
venn3(subsets = (1, 1, 1, 1, 1, 1, 1), set_labels = ('A', 'B', 'C'), ax = axes[1][0])
# 4:
venn3_circles({'001': 10, '100': 20, '010': 21, '110': 13, '011': 14}, ax = axes[1][1])

#plt.savefig('Venn_Diagram_2_1.png')
plt.show()

## ========== ##
## EXAMPLE  2 ##
## ========== ##

# define 3 sets from 3 lists:
set1 = set(['A', 'B', 'C', 'D'])
set2 = set(['B', 'C', 'D', 'E'])
set3 = set(['C', 'D',' E', 'F', 'G'])

venn3([set1, set2, set3], ('Set1', 'Set2', 'Set3'))

plt.title('Example 2')
#plt.savefig('Venn_Diagram_2_2.png')
plt.show()

## ========== ##
## EXAMPLE  3 ##
## ========== ##

# define 4 sets from 3 list:
S1 = set(['Jose', 'Juan', 'Pepe', 'Luisa', 'Marta'])
S2 = set(['Jose', 'Pere', 'Pepe', 'Joan', 'Marta'])
S3 = set(['Marta', 'María Luisa'])

venn3([S1, S2, S3], ('Grupo 1', 'Grupo 2', 'Grupo 3'))

plt.title('Example 3')
#plt.savefig('Venn_Diagram_2_3.png')
plt.show()