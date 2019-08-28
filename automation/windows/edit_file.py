import os
import fileinput

def changeCofigVersion():
  lines = 0
  offset = 0
  content = 0
  # adjust = 4
  oldVersion = 0
  newVersion = 0
  newData = ''

  os.chmod('../config.js', 0o777)

  with open('../config.js', 'r') as fd:
    for lno, line in enumerate(fd, 1):
      if 'APP_VERSION: ' in line:
        lines = lno
        break

    fd.seek(offset)
    content = fd.read()
    subString = 'APP_VERSION: '

    if content:
      offset = content.find(subString, offset, len(content) -1)

      if offset > 0:
        offset = offset + len(subString) + lines 
        fd.seek(offset)
        oldVersion = fd.read(8)
        oldVersion = oldVersion.split('\'')
        oldVersion = oldVersion[0]
        print('oldVersion:', oldVersion)
        arr = oldVersion.split('.')
        arr[len(arr)-1] = str(int(arr[len(arr)-1]) + 1)
        newVersion = '.'.join(arr)
        print('newVersion:', newVersion)

        newData = content.replace(oldVersion, newVersion)

    fd.close()

  with open('../config.js', 'w') as file:
    file.write(newData)

def changeUpdateVersion():
  lines = 0
  offset = 0
  content = 0
  oldVersion = 0
  newVersion = 0
  adjust = 3
  newData = ''

  os.chmod('../uxfme-update-config.json', 0o777)

  with open('../uxfme-update-config.json', 'r') as fd:
    for lno, line in enumerate(fd, 1):
      if 'updateversion' in line:
        lines = lno
        print(lines)
        break

    fd.seek(offset)
    content = fd.read()
    subString = 'updateversion'

    if content:
      offset = content.find(subString, offset, len(content) -1)

      if offset > 0:
        offset = offset + len(subString) + lines + adjust
        fd.seek(offset)
        oldVersion = fd.read(8)
        oldVersion = oldVersion.split('\"')
        oldVersion = oldVersion[0]
        print('oldVersion:', oldVersion)
        arr = oldVersion.split('.')
        arr[len(arr)-1] = str(int(arr[len(arr)-1]) + 1)
        newVersion = '.'.join(arr)
        print('newVersion:', newVersion)

        newData = content.replace(oldVersion, newVersion)

    fd.close()

  with open('../uxfme-update-config.json', 'w') as file:
    file.write(newData)
    pass

def main():
  # changeCofigVersion()
  # changeUpdateVersion()
  pass

if __name__ == "__main__":
  main()
