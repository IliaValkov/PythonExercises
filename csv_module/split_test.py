import csv_splitter

# csv_splitter.split(open("insurance_sample.csv", "r"),row_limit=501)

count = sum(1 for row in open("output_4.csv", "r"))
print(count)