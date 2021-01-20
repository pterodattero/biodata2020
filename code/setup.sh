echo "Installing BLAST..."
wget -P ../binx/ ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.11.0+-x64-linux.tar.gz
tar -xf ../binx/ncbi-blast-2.11.0+-x64-linux.tar.gz -C ../binx/
rm ../binx/ncbi-blast-2.11.0+-x64-linux.tar.gz

echo "Downloading SwissProt DB..."
wget -P ../data/db/ ftp://ftp.expasy.org/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
gunzip ../data/db/uniprot_sprot.fasta.gz
rm ../data/db/uniprot_sprot.fasta.gz

# Create database (Blast indexes, phr+pin+psq files)
../binx/ncbi-blast-2.11.0+/bin/makeblastdb -dbtype prot -in ../data/db/uniprot_sprot.fasta

echo "Installing HMMER..."
wget -P ../binx/ http://eddylab.org/software/hmmer/hmmer-3.3.1.tar.gz
tar -xf ../binx/hmmer-3.3.1.tar.gz -C ../binx/
rm ../binx/hmmer-3.3.1.tar.gz
cd ../binx/hmmer-3.3.1/ && ./configure && make

echo "Getting T-Coffee wrapper..."
wget ../code/ https://raw.githubusercontent.com/ebi-wp/webservice-clients/master/python/tcoffee.py

echo "Getting PDBs..."
wget -P ../data/ ftp://ftp.ebi.ac.uk/pub/databases/msd/sifts/flatfiles/csv/uniprot_pdb.csv.gz
tar -xf ../data/uniprot_pdb.csv.gz ../data/
rm ../data/uniprot_pdb.csv.gz

echo "Installing TM-Align..."
wget -P ../binx/ https://zhanglab.ccmb.med.umich.edu/TM-align/TMalign.gz
gunzip ../binx/TMalign.gz
rm ../binx/TMalign.gz
sudo chmod 777 ../binx/TMalign

echo "Getting CATH DB..."
wget -P ../data/ ftp://orengoftp.biochem.ucl.ac.uk/cath/releases/daily-release/newest/cath-b-newest-all.gz
wget -P ../data/ ftp://ftp.ebi.ac.uk/pub/databases/msd/sifts/flatfiles/csv/pdb_chain_cath_uniprot.csv.gz

echo "Getting SwissProt DB .xml file..."
wget -P ../data/ ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz

echo "Getting gene ontology..."
wget -P ../data/ http://purl.obolibrary.org/obo/go.obo

echo "Done."