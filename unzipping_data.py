import subprocess

# Use system unzip command which supports more compression methods
subprocess.run(['unzip', '-o', 'dataset_additional_riib.zip'], check=True)
