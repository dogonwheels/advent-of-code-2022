from common import register_over_time


signals = register_over_time("10/input")[19::40]
strength = sum([(20 + (index * 40)) * value for (index, value) in enumerate(signals)])

print(strength)
