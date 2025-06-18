#!/bin/bash
echo "[*] Running John the Ripper..."
john --wordlist=wordlists/custom.txt hashes/sample_hashes.txt
echo "[*] Cracked Passwords:"
john --show hashes/sample_hashes.txt > results/cracked.txt
cat results/cracked.txt
