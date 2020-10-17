import subprocess
from pip._internal.vcs import git
import sys
result=subprocess.run(["C:.git","import git;print_directory()", "import time; time.sleep(1)"], timeout=10,capture_output=True, text=True)
print("stdout:",result.stdout)
print("stderr:",result.stderr)