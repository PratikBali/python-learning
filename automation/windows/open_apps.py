import os
import subprocess

def openFiles():

  # open one note 2016
  one_note_path = r'C:\Program Files (x86)\Microsoft Office\root\Office16\ONENOTE.EXE'
  os.startfile(one_note_path)

  # open chrome with security flag false
  chrome_command = 'chrome.exe  --disable-web-security --allow-access-from-files --user-data-dir --profile-directory=Default'
  # os.system(chrome_command)
  # subprocess.run(chrome_command)

  # open perforce 
  p4v_path = 'C:\Program Files\Perforce\p4v.exe'
  os.startfile(p4v_path)


def main():
  openFiles()

if __name__ == '__main__':
  main()
