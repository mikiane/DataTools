import csv

# List of file names
filenames = ['file1.csv', 'file2.csv', 'file3.csv']

# Open the output file
with open('output.csv', 'w', newline='') as outfile:
  # Create a CSV writer
  writer = csv.writer(outfile)

  # Iterate over the input files
  for fname in filenames:
    # Open the input file
    with open(fname, 'r') as infile:
      # Create a CSV reader
      reader = csv.reader(infile)

      # Write the rows from the input file to the output file
      for row in reader:
        writer.writerow(row)
