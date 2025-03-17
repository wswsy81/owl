import matplotlib.pyplot as plt

# Data for plotting
labels = ['Stars', 'Forks']
values = [10431, 1070]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=['blue', 'orange'])

# Adding title and labels
plt.title('GitHub Repository Metrics for camel-ai/camel')
plt.xlabel('Metrics')
plt.ylabel('Count')

# Save the plot to a file
output_filename = 'camel_metrics.png'
plt.savefig(output_filename)

print(f'Bar chart saved as {output_filename}')