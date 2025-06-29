import paramiko

host = '127.0.0.1'
user = 'matheus'
passwd = 'televisao12345'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)



while True:
    stdin, stdout, stderr = client.exec_command(input('cmd: '))

   
    
    
    for line in stdout.readlines():
        print(line.strip())
        
        
