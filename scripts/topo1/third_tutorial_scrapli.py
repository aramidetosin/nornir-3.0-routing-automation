from scrapli.driver.core import IOSXEDriver


switch = {
    "host": "172.16.100.168",
    "auth_username": "admin",
    "auth_password": "admin",
    "auth_strict_key": False
}

cli = IOSXEDriver(**switch)
cli.open()
sh_int = cli.send_command("show ip ospf int brief")
print(sh_int.result)