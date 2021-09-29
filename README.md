# Stimulating-a-Petri-dish-in-Python


Stimulating a petri dish with size nxn and where each cell is either populated with one of 3 different Bacteria or empty for a 100 year period where each bacteria can make one of the three following actions to the ba:
1-Movement--> moving to a neighbor empty cell, original cell will be empty
2-Reproduction--> Reproducing to a neighbor empty cell, both cells with be populated with the bacteria.
3-Destruction--> It destroys the bacteria which populated the neighboring cell previously.

The neighboring cell is found randomly within a maximum of 7 tries. If it fails to find a cell other which is not populated from the same bacteria than it tries again the next day.
