import os

def main():
  uat = r'C:\private\perforce_branches\TEF-Peru-mobile-app\Tef_Peru_Mobile_App_2850_UAT\mobile_app\app'

  os.chdir(uat)
  print(uat + '\grunt dev')
  os.system("grunt dev")

if __name__ == "__main__":
    main()