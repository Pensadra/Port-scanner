from socket import *
from rich.console import Console

console = Console()
console.rule("[bold red]Port scaner by sadra")

ip = input("Enter The IP: ")
List = [80, 443, 445, 21, 23, 22, 3389, 3306]

console.print(f"|results for {ip}|", style="blink", justify="center")

for port in List:
    s = socket(AF_INET, SOCK_STREAM)
    result = s.connect_ex((ip, port))

    if result == 0:
        console.print("Port is open; ", port, style="bold green")

    else:
        console.print("port is close; ", port, style="bold red")

console.print("operation complete!", style="blue on white")
console.rule("[bold red]...")


