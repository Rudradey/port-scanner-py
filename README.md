# port-scanner-py
This Python script is a simple port scanner that utilizes the Nmap tool for scanning open ports on a specified website.

Port Scanner using Nmap

This Python script is a basic port scanner that leverages the Nmap tool to identify open ports on a specified website. The tool provides a simple interface for users to input a website URL and initiates a port scan using both xterm and the command-line interfaces.

Prerequisites

Ensure that you have Nmap installed on your system before running the script. You can install it by following the instructions on the official Nmap website: Nmap Installation

Additionally, the script relies on the termcolor module for colorful console output. You can install it using the following command:

pip install termcolor


Usage

Clone the repository:

git clone https://github.com/Rudradey/port-scanner-py.git


cd port-scanner

Run the script:

python port_scanner.py

Follow the prompts to input the target website URL.

The script will initiate a port scan using both xterm and the command-line interfaces, displaying the results.

Features

User-friendly interface for entering the target website.
Utilizes Nmap for efficient and comprehensive port scanning.
Supports interruption handling to ensure a smooth user experience.
Colorful console output for improved readability.
Notes
This script is designed for basic port scanning purposes and may not cover all edge cases or specific scenarios.
Use responsibly and ensure compliance with relevant laws and regulations when scanning external websites.
Disclaimer
This tool is provided for educational and informational purposes only. Use it responsibly and ethically. The authors are not responsible for any misuse or illegal activities performed with this tool.
