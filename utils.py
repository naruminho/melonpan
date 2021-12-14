import subprocess 
import shlex
import io

def run(command: str)->int:
    p = subprocess.run(shlex.split(command), capture_output=True)
    
    print(p)

run("ls -l")


