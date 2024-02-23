# Created by Ethan PP Cutting - 100942775
# importing subprocess so it will run new codes and applications by creating new processes
import subprocess
#
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for profile in profiles:
    # Handling special characters in profile names
    profile_name = profile.replace(" ", "_")  # Replace spaces with underscores
    results = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'], capture_output=True, text=True)
    
    if results.returncode == 0:
        output_lines = results.stdout.split('\n')
        key_content = [line.split(":")[1][1:-1] for line in output_lines if "Key Content" in line]
        if key_content:
            print("{:<30}|  {:<}".format(profile, key_content[0]))
        else:
            print("{:<30}|  {:<}".format(profile, ""))
    else:
        print("{:<30}|  {:<}".format(profile, "Encoding Error"))

input("")