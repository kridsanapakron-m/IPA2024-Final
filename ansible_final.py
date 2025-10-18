import subprocess
import os
import re

def showrun():
    student_id = "66070006"
    playbook_file = "playbook_showrun.yaml"
    temp_output = "temp_show_run.txt" 
    try:

        command = ["ansible-playbook", playbook_file]
        result = subprocess.run(command, capture_output=True, text=True)

        if "failed=0" in result.stdout:
            if not os.path.exists(temp_output):
                possible_files = [f for f in os.listdir(".") if f.startswith("show_run") and f.endswith(".txt")]
                if possible_files:
                    temp_output = possible_files[0]
                else:
                    print("ตรงนี้่1")
                    return "Error: Ansible"

            with open(temp_output, "r") as f:
                content = f.read()

            match = re.search(r"^hostname\s+(\S+)", content, re.MULTILINE)
            if match:
                router_name = match.group(1)
            else:
                router_name = "UnknownRouter"

            output_filename = f"show_run_{student_id}_{router_name}.txt"
            os.rename(temp_output, output_filename)

            return "ok"
        else:
            print("ตรงนี้่2")
            return "Error: Ansible"

    except Exception as e:
        print("ตรงนี้่3")
        return "Error: Ansible"
