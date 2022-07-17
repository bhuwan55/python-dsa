"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

"""

#ANS

expenses = [2200,2350,2600,2130,2190]

"""
1. In Feb, how many dollars you spent extra compare to January?
"""

print(expenses[2]-expenses[1])

"""
2. Find out your total expense in first quarter (first three months) of the year.
"""

quarter_total = 0
for i in range(3):
    quarter_total += expenses[i]
print(quarter_total)


"""
3. Find out if you spent exactly 2000 dollars in any month?
"""

quarter_total = 0
for expense in expenses:
    if expense == 2000:
        print(quarter_total)

"""
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list.
"""
expenses.append(1980)

"""
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this.
"""

expenses[3] = expenses[3] - 200