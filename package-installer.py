from googlesearch import search
from bs4 import BeautifulSoup
from subprocess import run
from colorama import Fore, Style, init
import sys, getopt, requests, os

def parse_inputs(opts):
    for opt, arg in opts:
        if opt == '-h':
            print(Fore.YELLOW + 'python package-installer.py -e <conda environment> -p <package name>' + Fore.RESET)
            sys.exit()
        elif opt in ("-e"):
            env = arg
        elif opt in ("-p"):
            query = "How to install {package_name} conda".format(package_name=arg)
    return env, query

def get_commands(query):
    commands = []
    for url in search(query, tld="com", num=10, stop=10, pause=2):
        if "anaconda.org" in url :
            print("using commands from: " + url + '\n')
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, "html.parser")
            for code in soup.find_all('code'):
                commands.append(code.get_text().lstrip().rstrip())
            return commands



def main():
    try:
        init(convert=True)
        os.system("mode 360")
        opts, _ = getopt.getopt(sys.argv[1:],"e:p:")
        env, query = parse_inputs(opts)
        commands = get_commands(query)
        for command in commands:
            cmd = command + " -y -n " + env
            print(cmd)
            userinput = input(Style.BRIGHT + Fore.RED + "Use this command? (y/n): " + Style.NORMAL + Fore.RESET)
            if(userinput == "y"):
                proc = run(cmd,
                text=True, capture_output=True)
                return print(proc.stdout)
        print(Fore.LIGHTYELLOW_EX + "\nNo packages installed!\n" + Fore.RESET)
    except getopt.GetoptError:
        print(Fore.YELLOW + 'python package-installer.py -e <conda environment> -p <package name>' + Fore.RESET)
        sys.exit(2)
if __name__ == "__main__":
    main()