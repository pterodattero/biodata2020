# Install blast (linux build 64bit)
echo "Installing BLAST..."
wget -P ../binx/ ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.11.0+-x64-linux.tar.gz
tar -xf ../binx/ncbi-blast-2.11.0+-x64-linux.tar.gz -C ../binx/
rm ../binx/ncbi-blast-2.11.0+-x64-linux.tar.gz

# Download SwissProt sequence
echo "Downloading SwissProt DB..."
wget -P ../data/db/ ftp://ftp.expasy.org/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
gunzip ../data/db/uniprot_sprot.fasta.gz
rm ../data/db/uniprot_sprot.fasta.gz

# Create database (Blast indexes, phr+pin+psq files)
../binx/ncbi-blast-2.11.0+/bin/makeblastdb -dbtype prot -in ../data/db/uniprot_sprot.fasta

# Download and compile HMMER
echo "Installing HMMER..."
wget -P ../binx/ http://eddylab.org/software/hmmer/hmmer-3.3.1.tar.gz
tar -xf ../binx/hmmer-3.3.1.tar.gz -C ../binx/
rm ../binx/hmmer-3.3.1.tar.gz
cd ../binx/hmmer-3.3.1/ && ./configure && make

# Get T-Coffee Python Wrapper
echo "Getting T-Coffee wrapper..."
wget ../code/ https://raw.githubusercontent.com/ebi-wp/webservice-clients/master/python/tcoffee.py

 Get PDB database
echo "Getting PDBs..."
wget -P ../data/ ftp://ftp.ebi.ac.uk/pub/databases/msd/sifts/flatfiles/csv/uniprot_pdb.csv.gz
tar -xf ../data/uniprot_pdb.csv.gz ../data/
rm ../data/uniprot_pdb.csv.gz

# Download TM-Align
echo "Installing TM-Align..."
wget -P ../binx/ https://zhanglab.ccmb.med.umich.edu/TM-align/TMalign.gz
gunzip ../binx/TMalign.gz
rm ../binx/TMalign.gz
sudo chmod 777 ../binx/TMalign

# Get CATH files...
echo "Getting CATH DB..."
wget -P ../data/ ftp://orengoftp.biochem.ucl.ac.uk/cath/releases/daily-release/newest/cath-b-newest-all.gz
wget -P ../data/ ftp://ftp.ebi.ac.uk/pub/databases/msd/sifts/flatfiles/csv/pdb_chain_cath_uniprot.csv.gz

# Get SwissProt
echo "Getting SwissProt DB .xml file..."
wget -P ../data/ ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz

echo "Done."