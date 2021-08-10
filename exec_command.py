# import os

# with open('./final-command_tintuc.txt', 'r') as f:
#     for line in f:
#         p = os.system('sudo -S %s' % (line))

import subprocess

with open('./final-command_tintuc.txt', 'r') as f:
    for line in f:
        subprocess.Popen("sudo bash -S %s" % (line), shell=True)
