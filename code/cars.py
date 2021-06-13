#sort()永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)

#sorted()临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars, reverse = True))
print(cars)

#列表反转，不是排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

#确定列表长度
print(len(cars))