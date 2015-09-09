# setwd("D:/Python34")

num_adoption <- read.table("num_bandadopt.csv",header = FALSE, sep = ",")
mfpairs <- read.table("adoptionpairs.csv",header = FALSE, sep = ",")
mfpairs_mod <- read.table("adoptionpairs_mod.csv",header = FALSE, sep = ",")

mfpairs <- mfpairs[,1]
week_diff <- mfpairs_mod[,1]
num_adoption <- num_adoption[,1]
mean(num_adoption)

# min(num_adoption) = 1
hist(num_adoption,breaks = 300,xlab = "num of bands adopted", ylab ="num of individuals")

table(num_adoption)

# min(mfpairs) = 0
hist(mfpairs,breaks = 300, 
     xlab = "num of bands adopted by both", ylab ="num of member/friend pairs")

table(mfpairs)

#
b <- c(-423, -16, -8, -4, 0, 4, 8, 16, 423)
cutweek_diff = cut(week_diff, breaks=b)
table(cutweek_diff)
barplot(table(cutweek_diff))

b <- c(-423, -52, -16, -8, -4, 0, 4, 8, 16, 52, 423)
cutweek_diff = cut(week_diff, breaks=b)
table(cutweek_diff)
barplot(table(cutweek_diff))

barplot(table(week_diff))

#
abs_week_diff <- abs(week_diff)
table(abs_week_diff)
barplot(table(abs_week_diff))

# number of adoptions by members
member_ids <- read.table("row_mid.csv",header = FALSE, sep = ",")
member_adoption_count <- c()
for (i in member_ids){
  member_adoption_count <- c(member_adoption_count, num_adoption[i])
}
member_ids <- t(member_ids)
madopt <- data.frame(member_ids,member_adoption_count)
# sort(member_adoption_count, decreasing = TRUE)
# on average members adopt more bands (and earlier) than non members(their friends)
mean(member_adoption_count)                       
hist(member_adoption_count,labels = TRUE, breaks = 20)
b <- which(member_adoption_count>100)
member_ids[b]

# number of overlapping adoptions by members (with their friends)
friendlist <- read.table("friends3.csv",header = FALSE, sep = ",")
num_overlaps <- matrix(0,nrow=0,ncol=2)
new_member <- friendlist[1,]
sum_overlap_adopt <- mfpairs[1]
for (i in 2:nrow(friendlist)){
  old_member <- new_member
  new_member <- friendlist[i,]
  if (old_member[1,1]==new_member[1,1]){
    sum_overlap_adopt <- sum_overlap_adopt + mfpairs[i]
  }
  else {
    num_overlaps <- rbind(num_overlaps,c(old_member[1,1],sum_overlap_adopt))
    sum_overlap_adopt <- mfpairs[i]
  }
}
num_overlaps <- rbind(num_overlaps,c(new_member[1,1],sum_overlap_adopt))   # last member

new_overlap <- num_overlaps[(num_overlaps[,1] %in% member_ids),]   # select members that are in member_ids
sum(new_overlap[,2])==sum(mfpairs)                                 # test

mean(new_overlap[,2])
hist(new_overlap[,2],labels = TRUE, breaks = 100)
sum(new_overlap[,2]<50)
sum(new_overlap[,2]<100)

# number of unduplicated overlapping adoptions by members (with their friends)
num_overlapping <- read.table("num_overlap_adopt.csv",header = FALSE, sep = ",")
mean(num_overlapping[,2])

hist(num_overlapping[,2],labels = TRUE, breaks = 20)
sum(num_overlapping[,2]>100)
b <- which(num_overlapping[,2]>100)
members_for_dummies <- num_overlapping[b,]

write.table(members_for_dummies, "members_for_dummies.csv", 
            row.names=F, col.names=F, sep=",")


#
bands_time <- read.table("tbands3.csv",header = FALSE, sep = ",")
band_obs_duration <- bands_time[,3]-bands_time[,2]+1
hist(band_obs_duration,labels = TRUE, breaks = 20)  
# meaning that many old bands was not listened by any user in the first two years

users_time <- read.table("tsplit3.csv",header = FALSE, sep = ",")
users_obs_duration <- users_time[,4]-users_time[,2]+1
hist(users_obs_duration,labels = TRUE, breaks = 20)

# count number of friends of each member
num_friends <- matrix(0,nrow=nrow(madopt),ncol=2)
old_member <- friendlist[1,1]
row_ind <- 1
count_f <- 1
for (i in 2:nrow(friendlist)){
  new_member <- friendlist[i,1]
  if (old_member==new_member){
    count_f <- count_f + 1
  }
  else {
    if (old_member %in% madopt$member_ids){
      num_friends[row_ind,1] <- old_member
      num_friends[row_ind,2] <- count_f
      row_ind <- row_ind + 1
    }      
    count_f <- 1
  }
  old_member <- new_member
}
num_friends[row_ind,1] <- old_member
num_friends[row_ind,2] <- count_f  # last member

num_friends[,1]==madopt[,1]        # check if the two have the same member ids

# crosstab of number of friends and number of adoptions
madopt <- cbind(madopt,num_friends[,2])

# b <- seq(1,2000,200)
b <- seq(1,2000,50)
numfriends_cat <- cut(madopt[,3],breaks = b)
min(madopt[,2])
max(madopt[,2])
# b <- seq(1,2000,200)
b <- seq(1,2000,50)
numadopts_cat <- cut(madopt[,2],breaks = b)
table(numfriends_cat,numadopts_cat)

#try <- c()
#for (i in 1:10){
#  try <- c(try,i)
#}

# select members to create dummies
obsbound <- madopt[,2]*madopt[,3]>50
d_individuals <- madopt[which(obsbound != 0),]

# sort members according to num_friends*num_adoptions
members_sort <- madopt[order(madopt[,2]*madopt[,3],decreasing = TRUE),]
