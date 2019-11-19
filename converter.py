
import csv

fileName = 'il-places'
# code for parsing CSV into a list of dictionaries taken from stackoverflow
# Thread: https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries
# response author: https://stackoverflow.com/users/2225682/falsetru
with open(fileName + '.csv') as csvFile:
    dataList = [{key: value for key, value in row.items()}
        for row in csv.DictReader(csvFile, skipinitialspace=True)]

# write to a js file after inserting export, const dec and array name
# massage data by deleting flagged quotes (~) around keys, replacing single quotes
with open(fileName + '.js', 'w') as jsFile:
    jsFile.write(format(str("export const PLACES = " +
    str(dataList).replace("'~", "")
    .replace("~'", "")
    .replace(": '", ': "')
    .replace("',", '",')
    .replace("'}", '"}') +";")))
