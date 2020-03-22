table <- read.csv("blastn_results_matrix_sorted.csv", sep="\t", row.names=1)
data <- as.matrix(table)

barplot(data, beside=TRUE, col=rainbow(19), ylab="number of hits for taxon (assumned abundance of bacterial species)", cex.names=0.3, las=2)
legend("topright", legend=rownames(data), cex=0.7, fill=rainbow(19))

