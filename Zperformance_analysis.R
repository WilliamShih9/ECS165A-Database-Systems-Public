library(tidyverse)
library(readxl)


res = cbind(index = 1, read.delim("performance1v0.csv", header=FALSE))
res = rbind(res, cbind(index = 2, read.delim("performance2v0.csv", header=FALSE)))
res = rbind(res, cbind(index = 3, read.delim("performance3v0.csv", header=FALSE)))
res = rbind(res, cbind(index = 4, read.delim("performance4v0.csv", header=FALSE)))
res = rbind(res, cbind(index = 5, read.delim("performance5v0.csv", header=FALSE)))  

insert = res[,1:2]
update = res[,c(1, 3)]
select = res[,c(1, 4)]
delete = res[,c(1, 5)]

withindex = cbind(index = "No index", read.delim("performance_selectsum_without_index.csv", header = FALSE))
indexing = rbind(withindex, cbind(index = "Index", read.delim("performance_selectsum_with_index.csv", header = FALSE))

insert_index = indexing[,1:2]
sum_index = indexing[,c(1,3:7)]
colnames(sum_index) = c("Index", "01%", "05%", "10%", "20%", "30%")
sum_index = sum_index %>%
  pivot_longer(cols = 2:6)
data_median = insert_index %>%
  group_by(index) %>%
  summarise(MD = median(V1))
sum_median =  sum_index %>%
  group_by(Index, name) %>%
  summarise(MD = median(value))
sum_median[3] = round(sum_median[3], 3)
data_median[2] = round(data_median[2], 3)
ggplot(insert_index, aes(x = index, group = index, y = V1)) +
  geom_boxplot(color = "red", fill = "orange", alpha = 0.2) +
  theme(legend.position="none") +
  theme_bw() +
  geom_text(data = data_median, aes(index, MD, label = MD), 
            position = position_dodge(width = 0.8)) +
  xlab("Index") +
  ylab("Time (seconds)") +
  ggtitle("Time Taken to select 1% of 10,000 rows of 5 columns (1,000 repeats)")
ggsave("IndexSelect.png", dpi = 300)


ggplot(sum_index, aes(x = name, dodge = Index, fill = Index, color = Index, y = value)) +
  geom_boxplot(alpha = 0.2, position = position_dodge(width = 0.5)) +
  theme(legend.position="none") +
  theme_bw() +
  geom_text(data = sum_median, aes(x = name, group = Index, MD, label = MD), 
            position = position_dodge(width = 0.5), color = "black") +
  xlab("Index") +
  ylab("Time (seconds)") +
  ggtitle("Time Taken to sum a subset of 10,000 rows (10 repeats)", subtitle = "1%, 5%, 10%, 20%, or 30% of rows")
ggsave("IndexSum.png", dpi = 300)

median_1 = insert %>%
  group_by(index) %>%
  summarise(MD = median(V1))
median_1[2] = round(median_1[2], 3)
ggplot(insert, aes(x = index, group = index,  y = V1)) +
  geom_boxplot(color = "red", fill = "orange", alpha = 0.2) +
  theme(legend.position="none") +
  theme_bw() +
  geom_text(data = median_1, aes(index, MD, label = MD), position =position_dodge(width = 0.8)) +
  xlab("Number of Indexes (1 index is just key column)") +
  ylab("Time (seconds)") +
  ggtitle("Time Taken to insert 10,000 rows of 5 columns by number of indexes")
ggsave('Insert.png', dpi = 300)


median_2 = update %>%
  group_by(index) %>%
  summarise(MD = median(V2))
median_2[2] = round(median_2[2], 3)
ggplot(update, aes(x = index, group = index,  y = V2)) +
  geom_boxplot(color = "red", fill = "orange", alpha = 0.2) +
  theme(legend.position="none") +
  theme_bw() +
  geom_text(data = median_2, aes(index, MD, label = MD), position =position_dodge(width = 0.8)) +
  xlab("Number of Indexes (1 index is just key column)") +
  ylab("Time (seconds)") +
  ggtitle("Time Taken to update 10,000 rows by number of indexes")
ggsave('Update.png', dpi = 300)


median_3 = select %>%
  group_by(index) %>%
  summarise(MD = median(V3))
median_3[2] = round(median_3[2], 3)
ggplot(select, aes(x = index, group = index,  y = V3)) +
  geom_boxplot(color = "red", fill = "orange", alpha = 0.2) +
  theme(legend.position="none") +
  theme_bw() +
  geom_text(data = median_3, aes(index, MD, label = MD), position =position_dodge(width = 0.8)) +
  xlab("Number of Indexes (1 index is just key column)") +
  ylab("Time (seconds)") +
  ggtitle("Time Taken to select 10,000 rows by number of indexes")
ggsave('Select.png', dpi = 300)


median_4 = delete %>%
  group_by(index) %>%
  summarise(MD = median(V4))
median_4[2] = round(median_4[2], 3)
ggplot(delete, aes(x = index, group = index,  y = V4)) +
  geom_boxplot(color = "red", fill = "orange", alpha = 0.2) +
  theme(legend.position="none") +
  theme_bw() +
  geom_text(data = median_4, aes(index, MD, label = MD), position =position_dodge(width = 0.8)) +
  xlab("Number of Indexes (1 index is just key column)") +
  ylab("Time (seconds)") +
  ggtitle("Time Taken to delete 10,000 rows by number of indexes")
ggsave('Delete.png', dpi = 300)
