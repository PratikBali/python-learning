import os

def main():
  sp11 = r'C:\private\perforce_branches\TEF-Peru-mobile-app\TEF_PERU_2930_sp11_PROD\mobile_app\app'

  os.chdir(sp11)
  print(sp11 + '\grunt dev')
  os.system("grunt dev")

if __name__ == "__main__":
    main()