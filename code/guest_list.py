guest_list = ['Excavator', 'blue_shit', 'huangff']
print(guest_list)

print("The person who cannot come is " + guest_list[2] + '.')
guest_list[2] = 'huangjj'
print(guest_list)

print("I found a bigger table.")
guest_list.insert(0, 'yanghh')
guest_list.insert(2, 'yangmm')
guest_list.append('yangbb')
print(guest_list)

print("Sorry, I can only invite two persons.")
first_del = guest_list.pop()
print("sorry, I cannot invite you, " + first_del.title() + '.')
second_del = guest_list.pop()
print("sorry, I cannot invite you, " + second_del.title() + '.')
third_del = guest_list.pop()
print("sorry, I cannot invite you, " + third_del.title() + '.')
forth_del = guest_list.pop()
print("sorry, I cannot invite you, " + forth_del.title() + '.')

print("you are invited, " + guest_list[0] + '.')
print("you are invited, " + guest_list[1] + '.')
del guest_list[1]
del guest_list[0]
print(guest_list)


