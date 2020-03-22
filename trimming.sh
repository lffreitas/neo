for file in fqs/*.fastq ; do
	echo $file
	fqs_trimmed=${file/fqs/fqs_trimmed}
	echo $fqs_trimmed
	reports=${file/fqs/reports}
	echo $reports

	./fastp --in1 ./$file --out1 ./$fqs_trimmed --html ./${reports/fastq/html} --json ./${reports/fastq/json} -q 20

done

echo "all done"
