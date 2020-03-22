for file in fasta_files/*.fasta ; do
	echo $file
	blastn=${file/fasta_files/blastn_results}

	blastn -db database/testdb -query $file -out ${blastn/fasta/csv} -outfmt "6 qseqid sseqid stitle evalue bitscore score pident" -max_target_seqs 10


done

echo "all done"
