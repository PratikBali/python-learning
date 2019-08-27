import os
import fileinput

# with fileinput.FileInput('../config.js', inplace=True, backup='.bak') as file:
#     for line in file:
#         print(line.replace('1.0.9', '1.0.8'), end='')

# f = open('../config.js','r')
# filedata = f.read()
# f.close()
# newdata = filedata.replace('ram', 'abcd')
# with open('../config.js', 'w') as file:
#   file.write(newdata)

def openFile():
  lines = 0

  with open('../config.js', 'r+') as f:
    for lno, line in enumerate(f, 1):
      if 'APP_VERSION: ' in line:
        print('lines', lno)
        lines = lno
        break
    f.close()

    try:
      fd = open('../config.js', 'r+')
    except IOError as io:
      print('File does not exist')
    else:
      print('File  exist')
      offset = 0
      content = fd.read()
      # lines = fd.readlines()
      subString = 'APP_VERSION: '


      
      if content:
        print('file length:', len(content))
        offset = content.find(subString, offset, len(content) -1)
        print('offset found:', offset)

        if subString in content:
          print('found at index:', content.index(subString))
          # print(lines)
          # print('found at line:', lines.index(subString))

        if offset > 0:
          fd.seek(offset + len(subString) + lines + 2)
          content = fd.read(3)
          print('content:', content)
          print('content convert:', float(content))
          content +=  1
          print('content incresed:', content)

        
        fd.close()

def main():
  pass
  openFile()

if __name__ == "__main__":
  main()
