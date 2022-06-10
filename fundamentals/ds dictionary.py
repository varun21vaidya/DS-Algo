list1={'jan':2200, 'feb':2350, 'march':2600, 'April':2130,'may':2190}
#getting values from keys
print(list1['jan'])

#getting keys from values
print(list(list1.keys())[list(list1.values()).index(2600)])