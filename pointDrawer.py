import re

# Your input string
input_string = "(Point(x=682.364, y=709.636), Point(x=678.18218, y=704.1814499999999), Point(x=673.6367300000001, y=697.8177999999999), Point(x=672.364, y=693.2724), Point(x=672.7276400000001, y=683.9996), Point(x=675.27309, y=679.636), Point(x=680.18218, y=675.9996), Point(x=685.6367300000001, y=673.636), Point(x=689.8185500000001, y=672.5450999999999), Point(x=694.5458, y=672.5450999999999), Point(x=698.5458, y=673.9996), Point(x=703.0913, y=676.5450999999999), Point(x=707.6367, y=680.3633), Point(x=710.5458, y=684.1814999999999), Point(x=711.6367, y=689.8177999999999), Point(x=710.9095, y=696.5450999999999), Point(x=708.1822000000001, y=701.636), Point(x=701.0913, y=709.636)) "

# Define a regular expression pattern to match Point(x=..., y=...)
pattern = re.compile(r'Point\((x=.*?),\s*(y=.*?)\)')

# Find all matches in the input string
matches = pattern.findall(input_string)

# Extract and round values from matches
result = [(round(float(match[0].split('=')[1])), round(float(match[1].split('=')[1]))) for match in matches]

# Print the result with commas between tuples
output_string = ', '.join([f'({pair[0]}, {pair[1]})' for pair in result])
print(output_string)
