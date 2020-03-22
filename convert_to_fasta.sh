for file in fqs_trimmed/*.fastq ; do
	echo $file
	fasta_folder=${file/fqs_trimmed/fasta_files}

	seqtk seq -a $file > ${fasta_folder/fastq/fasta}


done

echo "all done"
