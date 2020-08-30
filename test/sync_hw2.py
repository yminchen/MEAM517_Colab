"""
Synchronize homework files (either save files to google drive or copy files from github/google drive) 
"""
if 'google.colab' in str(get_ipython()):
  from google.colab import drive
  drive.mount('/content/drive')

  from os import path
  # Save files from Colab to Google drive
  if path.exists("quadrotor.py"):
      !cp quadrotor.py  drive/My\ Drive/MEAM517_colab/hw2/quadrotor.py 
      !cp quadrotor_generator.py drive/My\ Drive/MEAM517_colab/hw2/quadrotor_generator.py 
      !cp quad_sim.py drive/My\ Drive/MEAM517_colab/hw2/quad_sim.py 
      !cp trajectories.py drive/My\ Drive/MEAM517_colab/hw2/trajectories.py 
  # Read files to Colab
  else:
    # If the hw folder doesn't exist in google drive, create the folder and create new homework scripts
    if not path.exists("drive/My Drive/MEAM517_colab/hw2"):
      # create hw folder in google drive
      !mkdir drive/My\ Drive/MEAM517_colab/hw2
      # download homework scirpts to colab 
      !curl -s https://raw.githubusercontent.com/yminchen/MEAM517_Colab/test/test/quadrotor.py > quadrotor.py
      !curl -s https://raw.githubusercontent.com/yminchen/MEAM517_Colab/test/test/quadrotor_generator.py > quadrotor_generator.py
      !curl -s https://raw.githubusercontent.com/yminchen/MEAM517_Colab/test/test/quad_sim.py > quad_sim.py
      !curl -s https://raw.githubusercontent.com/yminchen/MEAM517_Colab/test/test/trajectories.py > trajectories.py
      # copy the new scripts to hw folder in google drive
      !cp quadrotor.py drive/My\ Drive/MEAM517_colab/hw2/quadrotor.py
      !cp quadrotor_generator.py drive/My\ Drive/MEAM517_colab/hw2/quadrotor_generator.py
      !cp quad_sim.py drive/My\ Drive/MEAM517_colab/hw2/quad_sim.py
      !cp trajectories.py drive/My\ Drive/MEAM517_colab/hw2/trajectories.py
    # Otherwise, copy the existing homework scirpts from google drive to colab
    else: 
      !cp drive/My\ Drive/MEAM517_colab/hw2/quadrotor.py quadrotor.py 
      !cp drive/My\ Drive/MEAM517_colab/hw2/quadrotor_generator.py quadrotor_generator.py 
      !cp drive/My\ Drive/MEAM517_colab/hw2/quad_sim.py quad_sim.py 
      !cp drive/My\ Drive/MEAM517_colab/hw2/trajectories.py trajectories.py 