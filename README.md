# neo

Please get fastp in the same folder:

`wget http://opengene.org/fastp/fastp`

`chmod a+x ./fastp`

Install BLAST:

`sudo apt install ncbi-blast+`

Install seqtk:

`sudo apt install seqtk`

Requires also Python 3 and R

Requires package "ape" for R


Given a a folder "fqs" with .fastq files and a "database" folder with a .fasta database of species, `./run_all.sh` outputs an OTU table with counts and a sorted table of the 50 most abundant bacteria  
