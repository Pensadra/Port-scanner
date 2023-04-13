import socket
from socket import *
from rich.console import Console
from datetime import datetime
import sys
import subprocess

subprocess.call("clear")

console = Console()
console.rule("[bold red]Port scanner by sadra")
try:
    ip = input("Enter The IP: ")
    List = [80, 443, 445, 21, 23, 22, 3389, 3306]

    console.print("-"*50, style="blue")
    console.print(f"|scanning {ip}|", style="blink", justify="center")
    console.print("-" * 50, style="blue")

    t1 = datetime.now()

    for port in List:
        s = socket(AF_INET, SOCK_STREAM)
        result = s.connect_ex((ip, port))

        if result == 0:
            console.print(f"port {port}:    open", style="bold green")

        else:
            console.print(f"port {port}:    close", port, style="bold red")

    console.print("operation complete!", style="blue on white")
    console.rule("[bold red]...")
    t2 = datetime.now()

    t3 = t2 - t1

    console.print(f"The operation was finished at {t3}")
except Exception as e:
    console.print("[!]Error:", e, style="bold red")
except KeyboardInterrupt:
    console.print("you have canceled the operation :|", style="bold red")
    sys.exit()
