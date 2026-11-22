from data import create_data
from diagram import show_histogram

analyze_data = create_data()

print("Antal värden:", len(analyze_data))

print("Värdena:", analyze_data)
print("Mina värden:", analyze_data)

show_histogram(analyze_data)