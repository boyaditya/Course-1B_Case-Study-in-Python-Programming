import statistics

# number of infections per day
infections = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# calculate statistics
min_infections = min(infections)
max_infections = max(infections)
range_infections = max_infections - min_infections
mean_infections = statistics.mean(infections)
median_infections = statistics.median(infections)
variance_infections = statistics.variance(infections)
std_dev_infections = statistics.stdev(infections)

# display statistics
print(f"Minimum: {min_infections}")
print(f"Maximum: {max_infections}")
print(f"Range: {range_infections}")
print(f"Mean: {mean_infections:.2f}")
print(f"Median: {median_infections}")
print(f"Variance: {variance_infections:.2f}")
print(f"Standard Deviation: {std_dev_infections:.2f}")