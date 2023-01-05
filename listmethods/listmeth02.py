#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)

# this line will add "dns" to the end of our list
proto.append("dns") 

# this line will add "dns" to the end of our list
protoa.append("dns") 

# a list of common ports
proto2 = [ 22, 80, 443, 53]

# pass proto2 as an argument to the extend method
proto.extend(proto2) 
print(proto)

# pass proto2 as an argument to the append method
protoa.append(proto2) 
print(protoa)

# Return the number of times http appears in the list.

count1 = proto.count('http')
count2 = protoa.count('http')
count3 = proto2.count('http')

x = [count1, count2, count3]
Sum = sum(x)
print('http occurences:', Sum)


