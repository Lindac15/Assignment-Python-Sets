# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:
# The destinations both airlines fly to.
# The destinations unique to your airline.
# Whether there are any destinations that neither airline shares.


our_routes = {"New York", "Paris", "London"}
competitor_routes = {"New York", "Sydney", "Paris"}

# The destinations both airlines fly to.
both_airlines = our_routes.intersection(competitor_routes)
print("The destinations both airlines fly to:", both_airlines)

# The destinations unique to your airline.
unique_airline = our_routes.difference(competitor_routes)
print("The destinations unique to your airline:", unique_airline)

# Whether there are any destinations that neither airline shares.
neither_airline = our_routes.symmetric_difference(competitor_routes)
print("Whether there are any destinations that neither airline shares:", neither_airline)


