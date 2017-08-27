from collections import namedtuple

"""Total growth factor of a city is computed by summing up health factor of each building and divided by the city's 
total population in each column."""
GrowthFactor = namedtuple('GrowthFactor', 'food health_care')
