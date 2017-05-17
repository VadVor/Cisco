import crassh


routers = ["13.79.232.71"]
username = "user_csr1000"
password = "********mm_01"

for device in routers:
    hostname = crassh.connect(device, username, password)
    output = crassh.send_command("show run | inc snmp-server community", hostname)
    crassh.disconnect()
words = output.split()
for x in words:
    if x == "public":
        print("DANGER: Public SNMP Community set on %s [%s]" % (hostname, device))

