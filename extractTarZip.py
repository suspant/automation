#!/usr/bin/python

#Code execution: python extractTarZip.py --f <filepath>

import argparse
import tarfile
import zipfile

parser=argparse.ArgumentParser()
parser.add_argument('--f', '--sourcefilePath', required=True, dest='filePath', type=str, help="file path to be extracted ")

args=parser.parse_args()
filePath=args.filePath

if (filePath.endswith("tar.gz")):
    tar = tarfile.open(filePath, "r:gz")
    tar.extractall()
    tar.close()
elif (filePath.endswith("tar")):
    tar = tarfile.open(filePath, "r:")
    tar.extractall()
    tar.close()
else:
    zip = zipfile.ZipFile(filePath)
    zip.extractall()