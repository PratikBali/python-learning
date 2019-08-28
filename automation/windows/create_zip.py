import os
import shutil

def createZip(inputPath, outputPath, zipName):
  print(zipName)
  shutil.make_archive(outputPath + zipName, 'zip', inputPath)

def copy(outputPath):
  updatePath = '../updateData'
  outputZipPath = '../' 
  filePath = '../uxfme-update-config.json'
  zipPath = outputPath + 'dist.zip'
  zipName = 'update'

  if not os.path.isdir(updatePath):
    os.mkdir(updatePath)

  shutil.copy(filePath, updatePath)
  shutil.copy(zipPath, updatePath)

  createZip(updatePath, outputZipPath, zipName)

def main():
  inputPath = r'C:\private\perforce_branches\TEF-Peru-mobile-app\SP2_2930\mobile_app\app\dist'
  outputPath = '../../automation/'
  zipName = 'dist'

  if not os.path.isabs(inputPath):
    inputPath = os.path.abspath(inputPath)

  if not os.path.isdir(outputPath):
    os.mkdir(outputPath)

  createZip(inputPath, outputPath, zipName)
  copy(outputPath)

if __name__ == '__main__':
    main()
