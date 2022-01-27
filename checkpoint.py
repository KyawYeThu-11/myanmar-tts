import os
import shutil
import argparse

# arguments
parser = argparse.ArgumentParser()
parser.add_argument('checkpoint_step', type=str, help='checkpoint step')
args = parser.parse_args()

# variables
checkpoint_name = 'step-{}'.format(args.checkpoint_step)
log_dir = '/root/mm-tts/logs-mmspeech'
checkpoint_dir = os.path.join(log_dir, checkpoint_name)

# move the zip file to log dir
os.makedirs('/root/mm-tts/logs-mmspeech/', exist_ok=True)
shutil.move('{}.zip'.format(checkpoint_name), '/root/mm-tts/logs-mmspeech/')

# unzip the zip file from log dir
os.chdir('/root/mm-tts/logs-mmspeech/')
os.system("unzip {}.zip".format(checkpoint_name))
os.system("rm {}.zip".format(checkpoint_name))

# move all files inside the folder to log dir
for file in os.listdir(checkpoint_dir):
  shutil.move(os.path.join(checkpoint_dir, file), log_dir)

# remove the empty folder
os.rmdir('/root/mm-tts/logs-mmspeech/{}'.format(checkpoint_name))
