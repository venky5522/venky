d = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
l = []
for i in d:
    for x,y in i.items():
        l.append(y)
print(set(l))



