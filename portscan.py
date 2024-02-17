import os
import sys
from termcolor import colored, cprint

def get_user_input():
    try:
        CORE_STRING = colored("[port_scanner]", 'blue')
        WEBSITE = input(CORE_STRING + " Website> ").strip()
        return WEBSITE

    except KeyboardInterrupt:
        cprint("\n[!] User aborted the scan!", 'red')
        sys.exit(0)
    except Exception as e:
        cprint(f"\n[!] Error: {e}", 'red')
        sys.exit(1)

def run_port_scanner(website):
    try:
        xterm_scan = f"xterm -e nmap --open {website}"
        os.system(xterm_scan)

        cli_string = f"nmap --open {website}"
        os.system(cli_string)

    except Exception as e:
        cprint(f"[!] Error: {e}", 'red')

def main():
    website = get_user_input()
    run_port_scanner(website)

if __name__ == "__main__":
    main()
