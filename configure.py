#!/usr/bin/env python
import os
from shutil import copy
import glob
import platform
import subprocess

EXT_PACKAGES = [
  '2gua.rainbow-brackets',
  'PKief.material-icon-theme',
  'dracula-theme.theme-dracula',
  'eamodio.gitlens',
  'octref.vetur',
  'oderwat.indent-rainbow',
  'riccardoNovaglia.missinglineendoffile',
  'shardulm94.trailing-spaces'
]

def check_vscode_existence():
  try:
    subprocess.call(['which', 'code'])
    return True
  except:
    return False

def install_extension(extension):
  subprocess.call(['code', '--install-extension', extension])

def prepare_folder(path):
  if not os.path.exists(path):
    os.makedirs(path)

def copy_files(from_location, to_location):
  for file in glob.glob(from_location):
    print('Copying {}...'.format(file))
    copy(file, to_location)

def install_font():
  target_location = '{}/.fonts'.format(os.path.expanduser('~'))
  prepare_folder(target_location)
  copy_files('./fonts/*.ttf', target_location)
  subprocess.call(['fc-cache', '-f', '-v'])

def configure_editor_preferences():
  target_location = '{}/.config/Code/User'.format(os.path.expanduser('~'))
  prepare_folder(target_location)
  copy_files('./preferences/*.json', target_location)

def main():
  if check_vscode_existence():
    print('Installing extensions...')
    for extension in EXT_PACKAGES:
      install_extension(extension)
    print('Installing fonts...')
    install_font()
    print('Sending profile preferences...')
    configure_editor_preferences()
    print('--------------')
    print('VSCode ready!')
    print('--------------')
  else:
    print('Please install VSCode, getting from: https://code.visualstudio.com')

if __name__ == '__main__':
  main()
