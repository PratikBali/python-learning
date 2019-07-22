import os
import webbrowser
import subprocess
from subprocess import check_output
import urllib


def openFiles():

  # open one note 2016
  one_note_path = r'C:\Program Files (x86)\Microsoft Office\root\Office16\ONENOTE.EXE'
  os.startfile(one_note_path)

  # open chrome with security flag false
  chrome_command = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe  --disable-web-security --allow-access-from-files --user-data-dir --profile-directory=Default'
  subprocess.check_output(chrome_command)

  # open perforce 
  p4v_path = r'C:\Program Files\Perforce\p4v.exe'
  os.startfile(p4v_path)

  # open internet explorer  
  ie_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
  os.startfile(ie_path)

  # open outlook 
  outlook_path = r'C:\Program Files (x86)\Microsoft Office\root\Office16\OUTLOOK.EXE'
  os.startfile(outlook_path)

  # open Visual studio code 
  code_path = r'C:\Users\pratibal\AppData\Local\Programs\Microsoft VS Code\Code.exe'
  os.startfile(code_path)


def main():
  openFiles()

if __name__ == '__main__':
  main()

# os.system(chrome_command)
# os.startfile(chrome_command)
# subprocess.run(chrome_command)
# subprocess.call(chrome_command, shell=True) 

# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# dev = 'file:///C:/private/perforce_branches/TEF-Peru-mobile-app/Telefonica_Peru_Mobileapp_4850_DEV/mobile_app/app/src/templates/layouts/screen.html'
# uat = 'C:/private/perforce_branches/TEF-Peru-mobile-app/Tef_Peru_Mobile_App_2850_UAT/mobile_app/app/src/templates/layouts/screen.html'
# sp10 = 'C:/private/perforce_branches/TEF-Peru-mobile-app/Tef_Peru_2930_sp10_6799_PROD/mobile_app/app/src/templates/layouts/screen.html'
# sp11 = 'C:/private/perforce_branches/TEF-Peru-mobile-app/TEF_PERU_2930_sp11_PROD/mobile_app/app/src/templates/layouts/screen.html'

# webbrowser.open(dev)
# webbrowser.open(uat, new = 2)
# webbrowser.open(sp10, new = 3)
# webbrowser.open(sp11, new = 4)
# webbrowser.open_new_tab(dev + 'doc/')
# webbrowser.get(chrome_path).open(dev)
# urllib.urlopen(dev).read()
# webbrowser.open('file://' + os.path.realpath(uat))

# open cmd
# dev = r'C:\private\perforce_branches\TEF-Peru-mobile-app\Telefonica_Peru_Mobileapp_4850_DEV\mobile_app\app'
# uat = r'C:\private\perforce_branches\TEF-Peru-mobile-app\Tef_Peru_Mobile_App_2850_UAT\mobile_app\app'
# sp10 = r'C:\private\perforce_branches\TEF-Peru-mobile-app\Tef_Peru_2930_sp10_6799_PROD\mobile_app\app'
# sp11 = r'C:\private\perforce_branches\TEF-Peru-mobile-app\TEF_PERU_2930_sp11_PROD\mobile_app\app'

# os.chdir(dev)
# os.system("start cmd /c {grunt dev}")
# os.system("start /B start cmd.exe @cmd /k grunt dev")

# os.chdir(uat)
# os.system("start cmd")
# os.chdir(sp10)
# os.system("start cmd")
# os.chdir(sp11)
# os.system("start cmd")