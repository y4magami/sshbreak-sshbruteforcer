# sshbreak-sshbruteforcer
SSH Brute Force Script

A Python script to demonstrate SSH brute force attacks using paramiko. For educational purposes only.
Features

    Tries username/password combinations from wordlists.

    Uses multithreading for speed.

    Clean output (hides non-critical errors).

Requirements

    Python 3.x

    Install paramiko:
    bash
    Copy

    pip install paramiko

Usage

    Create two files:

        usernames.txt: List of usernames (one per line).

        passwords.txt: List of passwords (one per line).

    Run the script:
    bash
    Copy

    python ssh_brute_force.py <target_ip> <usernames.txt> <passwords.txt> <threads>

Example:
bash
Copy

python ssh_brute_force.py 192.168.1.1 usernames.txt passwords.txt 5

Disclaimer

Use responsibly. Unauthorized access is illegal. Only test on systems you own or have permission to test.
