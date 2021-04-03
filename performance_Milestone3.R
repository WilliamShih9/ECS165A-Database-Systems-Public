

library(dplyr)
library(ggplot2)
performance <- read.csv("performance.csv", header=FALSE)
scores <- read.csv("Score.csv", header = FALSE)
scores2 = dplyr::filter(scores, grepl("Score", V1))
scores3 = apply(scores2, 1, function(x) substr(x, 7,10))
scores3[1] = 3000
scores3 = cbind(performance[1], scores3)
data_median = performance %>%
  group_by(V1) %>%
  summarise(MD = median(V3))
data_median[2] = round(data_median[2], 3)
scores_median = scores3 %>%
  group_by(V1) %>%
  summarise(MD = median(as.numeric(scores3)))
scores_median[2] = round(scores_median[2], 3)
ggplot(performance, aes(x = V1, group = V1, 
                                 y = V3)) +
                  geom_boxplot(color = "red", fill = "orange", alpha = 0.2) +
                  theme(legend.position="none") +
                  theme_bw() +
                  xlab("Number of Threads") +
                  ylab("Time (seconds)") +
                  geom_text(data = data_median, aes(V1, MD, label = MD), 
                            position = position_dodge(width = 0.8)) +
                  ggtitle("Time to do m3_tester_part_2.py with 3000 instead of 1000 by Number of Threads")
ggsave("Performance.png", dpi = 300)
ggplot(scores3, aes(x = V1, group = V1, 
                        y = as.numeric(scores3))) +
  geom_boxplot(color = "red", fill = "orange", alpha = 0.2) +
  theme(legend.position="none") +
  theme_bw() +
  xlab("Number of Threads") +
  ylab("Scores (out of 3000)") +
  geom_text(data = scores_median, aes(V1, MD, label = MD), 
            position = position_dodge(width = 0.8)) +
  ggtitle("Score out of 3000 m3_tester_part_2.py with 3000 instead of 1000 by Number of Threads")
ggsave("Score.png", dpi = 300)
