
thestring = "abcdefg"

# Way  1
the_list = list(thestring)
print the_list

# Way 2
for c in thestring:
    print c

# Way 3
results = [c for c in thestring]
print results

