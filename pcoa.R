library(ape)

table <- read.csv("blastn_results_matrix_sorted.csv", sep="\t", row.names=1)
data <- as.matrix(table)

distmatrix <- dist(data, method="euclidean")
out <- pcoa(distmatrix)
biplot(out)
