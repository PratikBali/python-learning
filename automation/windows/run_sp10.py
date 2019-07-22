import os

def main():
  sp10 = r'C:\private\perforce_branches\TEF-Peru-mobile-app\Tef_Peru_2930_sp10_6799_PROD\mobile_app\app'

  os.chdir(sp10)
  print(sp10 + '\grunt dev')
  os.system("grunt dev")

if __name__ == "__main__":
    main()