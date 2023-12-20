total = 0
expenses = []
num_expenses = int(input('Enter # of expenses:\n'))
for i in range(num_expenses):
    expenses.append(float(input('Enter an expense:\n')))
total = sum(expenses)
print('You spent $', total, sep = '')