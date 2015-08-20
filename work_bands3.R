num_adoption <- read.table("num_bandadopt.csv",header = FALSE, sep = ",")
mfpairs <- read.table("adoptionpairs.csv",header = FALSE, sep = ",")
mfpairs_mod <- read.table("adoptionpairs_mod.csv",header = FALSE, sep = ",")

mfpairs <- mfpairs[,1]
week_diff <- mfpairs_mod[,1]
num_adoption <- num_adoption[,1]

# min(num_adoption) = 1
hist(num_adoption,breaks = 300,xlab = "num of bands adopted", ylab ="num of individuals")

# min(mfpairs) = 0
hist(mfpairs,breaks = 300, 
     xlab = "num of bands adopted by both", ylab ="num of member/friend pairs")

#
b <- c(-423, -16, -8, -4, 0, 4, 8, 16, 423)
cutweek_diff = cut(week_diff, breaks=b)
table(cutweek_diff)
barplot(table(cutweek_diff))

b <- c(-423, -52, -16, -8, -4, 0, 4, 8, 16, 52, 423)
cutweek_diff = cut(week_diff, breaks=b)
table(cutweek_diff)
barplot(table(cutweek_diff))

braplot(table(week_diff))

