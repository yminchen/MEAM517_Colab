"""
Synchronize homework files (either save files to google drive or copy files from github/google drive) 
"""
import os
from os import path
from shutil import copyfile
import urllib.request

def sync_hw2():
  if 'google.colab' in str(get_ipython()):
    from google.colab import drive
    drive.mount('/content/drive')

    # Save files from Colab to Google drive
    if path.exists("quadrotor.py"):
      if not path.exists("drive/My Drive/MEAM517_colab/hw2"):
        # create hw folder in google drive
        # !mkdir drive/My\ Drive/MEAM517_colab/hw2
        os.mkdir('drive/My Drive/MEAM517_colab/hw2')
      copyfile("quadrotor.py",  "drive/My Drive/MEAM517_colab/hw2/quadrotor.py")
      copyfile("quadrotor_generator.py", "drive/My Drive/MEAM517_colab/hw2/quadrotor_generator.py")
      copyfile("quad_sim.py", "drive/My Drive/MEAM517_colab/hw2/quad_sim.py")
      copyfile("trajectories.py", "drive/My Drive/MEAM517_colab/hw2/trajectories.py")
    # Read files to Colab
    else:
      # If the hw folder doesn't exist in google drive, create the folder and create new homework scripts
      if not path.exists("drive/My Drive/MEAM517_colab/hw2"):
        # create hw folder in google drive
        # !mkdir drive/My\ Drive/MEAM517_colab/hw2
        os.mkdir('drive/My Drive/MEAM517_colab/hw2')
        # download homework scirpts to colab 
        urllib.request.urlretrieve("https://raw.githubusercontent.com/yminchen/MEAM517_Colab/test/test/quadrotor.py", "quadrotor.py")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/yminchen/MEAM517_Colab/test/test/quadrotor_generator.py", "quadrotor_generator.py")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/yminchen/MEAM517_Colab/test/test/quad_sim.py", "quad_sim.py")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/yminchen/MEAM517_Colab/test/test/trajectories.py", "trajectories.py")
        # copy the new scripts to hw folder in google drive
        copyfile("quadrotor.py",  "drive/My Drive/MEAM517_colab/hw2/quadrotor.py")
        copyfile("quadrotor_generator.py", "drive/My Drive/MEAM517_colab/hw2/quadrotor_generator.py")
        copyfile("quad_sim.py", "drive/My Drive/MEAM517_colab/hw2/quad_sim.py")
        copyfile("trajectories.py", "drive/My Drive/MEAM517_colab/hw2/trajectories.py")
      # Otherwise, copy the existing homework scirpts from google drive to colab
      else: 
        copyfile(  "drive/My Drive/MEAM517_colab/hw2/quadrotor.py", "quadrotor.py")
        copyfile( "drive/My Drive/MEAM517_colab/hw2/quadrotor_generator.py", "quadrotor_generator.py")
        copyfile( "drive/My Drive/MEAM517_colab/hw2/quad_sim.py", "quad_sim.py")
        copyfile( "drive/My Drive/MEAM517_colab/hw2/trajectories.py", "trajectories.py")