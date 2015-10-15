import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print '-' * 10
assert hashmap.get(cities, 'NY') == "New York"
print "NY state has: %s" % hashmap.get(cities, 'NY')
assert hashmap.get(cities, 'OR') == "Portland"
print "OR state has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
assert hashmap.get(states, 'Michigan') == 'MI'
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
assert hashmap.get(states, 'Florida') == 'FL'
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities hashmap
print '-' *10
hashmap.list(states)

# print every city in state
print '-' *10
hashmap.list(cities)

print '-' * 10
assert not hashmap.get(states, 'Texas')
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas."

# default values using ||=with the nil result
# can you do this on one line?
assert not hashmap.get(cities, 'TX')
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX is: %s" % city

print '-' * 10
hashmap.dump(states)
