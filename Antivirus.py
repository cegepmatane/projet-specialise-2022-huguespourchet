import hashlib
import json

# Détection de malware en utilisant 3 fonctions hash
import re


def hashScan_sha256(file):
    virus_found = False
    bytes = file.read()
    readable_hash = hashlib.sha256(bytes).hexdigest();
    with open("data/SHA256.txt",'r') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            if str(readable_hash) == str(line.split(";")[0]):
                virus_found = True
        f.close()
    return virus_found




def hashScan_md5(file):
    virus_found = False
    bytes = file.read()
    readable_hash = hashlib.sha256(bytes).hexdigest();
    with open("data/MD5 Virus Hashes.txt", 'r') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            if str(readable_hash) == str(line.split(";")[0]):
                virus_found = True
        f.close()
    return virus_found




def hashScan_sha1(file):
    virus_found = False
    bytes = file.read()
    readable_hash = hashlib.sha256(bytes).hexdigest();
    with open('data/SHA1 HASHES.json', 'r') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            if str(readable_hash) == str(line.split(";")[0]):
                virus_found = True
        f.close()
    return virus_found


#Detection par signature

def chekSignatures(file):
    signature = "virus"
    lines = file.readlines()
    for line in lines:
        if re.search(signature, line):
            return True
    return False
