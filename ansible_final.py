import subprocess
import os
import re

def showrun():
    playbook_file = "playbook_showrun.yaml"
    command = ["ansible-playbook", playbook_file]
    result = subprocess.run(command, capture_output=True, text=True)
    result = result.stdout
    if "failed=0" in result and 'unreachable=0' in result:
        return "ok"
    else:
        return "Error: Ansible"
