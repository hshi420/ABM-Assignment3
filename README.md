# Assignment3
The model’s purpose was to simulate the segregation by color in the US, and it assumes the agents’ only distinction to be twofold (Schelling, 1988). <br>

``run_batch.py`` is for running the model on batch, and can be run with the command line ``python run_batch.py``. <br>
``run_single1/2/3.py`` are for single runs, and can be run with the command line ``python run_single1/2/3.py``. <br>

The modification I made is to add a second dimension on segmentation factor -- wealth. I intended to explore whether the a second factor would affect the segmentaion on the agents' type. However, I did not check the two factors simultaneously, and I still check the type variable first. In addition, the segmentation measure is on average type similartiy.
