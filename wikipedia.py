import subprocess
import sys 
result=subprocess.run([sys.executable,"-c", "print('CV')","raise ValueError('oops')","import time; time.sleep(2)"], timeout=10,capture_output=True, text=True)
print("stdout:",result.stdout)
print("stderr:",result.stderr)