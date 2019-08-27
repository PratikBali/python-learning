import os

def main():
  sp12 = r'C:\private\perforce_branches\TEF-Peru-mobile-app\PROD_2930_sp12\mobile_app\app'

  os.chdir(sp12)
  print(sp12 + '\grunt dev')
  os.system("grunt dev")

if __name__ == "__main__":
    main()