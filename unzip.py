import os
import argparse

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-ckpt', '--checkpoint', type=bool, default=True, help="checkpoint zip file to unzip")
parser.add_argument('-e', '--event', type=bool, default=True, help="event zip file to unzip")
args = parser.parse_args()

log_dir = '/root/mm-tts/logs-mmspeech/'

# unzip the zip files to log directory and delete them thereafter
os.makedirs(log_dir, exist_ok=True)

if args.checkpoint:
    os.system(f'''
        unzip ckpt-*.zip -d {log_dir}
        rm ckpt-*.zip
    ''')

if args.event:
    os.system(f'''
        unzip events-*.zip -d {log_dir}
        rm events-*.zip
    ''')