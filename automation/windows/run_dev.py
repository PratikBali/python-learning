import os

def main():
  dev = r'C:\private\perforce_branches\TEF-Peru-mobile-app\Telefonica_Peru_Mobileapp_4850_DEV\mobile_app\app'

  os.chdir(dev)
  print(dev + '\grunt dev')
  os.system("grunt dev")

if __name__ == "__main__":
    main()
