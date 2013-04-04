def removeLineBreaks(filename, newfilename, numcolumns):
  f = open(filename)
  contents = f.read()
  f.close()
  #Split each cell into a list item
  contentsAsList = contents.split('\t')
  #Remove new lines from cell content and add to new string, row by row
  contentsAsString = ''
  columnCount = 1
  for cell in contentsAsList:
    if cell == contentsAsList[-1]:
      cellWithoutNewLines = cell.replace('\n',' ')
      contentsAsString += cellWithoutNewLines
    elif columnCount == numcolumns:
      #Find the split point (the last \n)
      splitpoint = cell.rfind('\n')
      #Split the cell to start a new row and remove newlines
      lastCell = cell[:splitpoint].replace('\n', ' ')
      firstCell = cell[splitpoint:].replace('\n', ' ')
      #Add the two cells in with a \n between them
      contentsAsString += lastCell
      contentsAsString += '\n'
      contentsAsString += firstCell
      contentsAsString += '\t'
      lastCell = ''
      firstCell = ''
      columnCount = 2
    else:
      cellWithoutNewLines = cell.replace('\n',' ')
      contentsAsString += cellWithoutNewLines
      contentsAsString += '\t'
      cellWithoutNewLines = ''
      columnCount += 1
  f = open(newfilename, 'w')
  f.write(contentsAsString)
  f.close()
  print "Success!"
  raw_input("Press Enter to exit.")


print """
This program will take your Tab Delimited txt file and prepare a new one for
Cvent import by removing line breaks within the cells.
Please contact Margaret with any issues you encounter.
"""

filename = raw_input("""
    Make sure your txt file is in the same directory as this program.
    Enter the name of your txt file. Do not include the file extension.

    """)+'.txt'


while 1:
  user_input = raw_input("""
    Please enter the number of columns in your file.

    """)
  try:
    numcolumns = int(user_input)
    break
  except ValueError:
    print "\nHey hey hey! That was not a number. You entered: " + user_input +'\n'
newfilename = raw_input("""
    This program will create a new txt file.
    Please enter the name you would like.

    """)+'.txt'

removeLineBreaks(filename,newfilename,numcolumns)

