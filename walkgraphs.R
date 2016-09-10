library(ggplot2)

allwalks <- read.csv("~/Desktop/allwalks.csv")
bbi<-element_text(face="bold.italic", color="black")

dumb <-ggplot(data=allwalks, aes(dumbSQ)) +
  geom_histogram(binwidth=1, fill=I("lightblue"), col=I("black")) + 
  theme(legend.position='none', title=bbi) + 
  xlab("Minutes") + ylab("Frequency") + 
  labs(title="Ten Thousand 8x8 Dumb Walks") +
  xlim(15,34) +
  ylim(0,4000)

smart <-ggplot(data=allwalks, aes(smartSQ)) +
  geom_histogram(binwidth=1, fill=I("lightblue"), col=I("black")) + 
  theme(legend.position='none', title=bbi) + 
  xlab("Minutes") + ylab("Frequency") + 
  labs(title="Ten Thousand 8x8 Smart Walks") + 
  xlim(15,34) +
  ylim(0,4000)

dumblib <-ggplot(data=gridwalks, aes(dumbLIB)) +
  geom_histogram(binwidth=1, fill=I("lightblue"), col=I("black")) + 
  theme(legend.position='none', title=bbi) + 
  xlab("Minutes") + ylab("Frequency") + 
  labs(title="Ten Thousand Dumb Walks to Library") +
  xlim(15,26) +
  ylim(0,5000)

smartlib <-ggplot(data=allwalks, aes(smartLIB)) +
  geom_histogram(binwidth=1, fill=I("lightblue"), col=I("black")) + 
  theme(legend.position='none', title=bbi) + 
  xlab("Minutes") + ylab("Frequency") + 
  labs(title="Ten Thousand Smart Walks to Library") + 
  xlim(15,26) +
  ylim(0,5000)

binom <- data.frame(0:16, dbinom(0:16, 16, 0.5))
names(binom) <- c("success", "prob")

dumbmodel <- ggplot(data=binom, aes(x=success, y=prob)) +
  geom_bar(stat="identity", fill=I("lightblue"), col=I("black"), width = 1)+
  theme(legend.position='none', title=bbi) + ylim(0,0.4) +
  labs(title="Ten Thousand 8x8 Dumb Walks [Model]") +
  xlab("Successes") + ylab("Probability")

turn <- function(x){
  r <- 0
  for(i in 0:(8-x)){ r <- r + dim(combn(7+i,i))[2]*(dim(combn(8-i,x))[2]) }
  r/2^15
}

success <- 0:8
combo <- data.frame(k, sapply(k,f))
combo[1,2] <- combo[1,2] - dim(combn(15,8))[2]*(dim(combn(1,0))[2])/32768
names(combo) <- c("success", "prob")

smartmodel <- ggplot(data=combo, aes(x=success, y=prob)) +
  geom_bar(stat="identity", fill=I("lightblue"), col=I("black"), width = 1)+
  theme(legend.position='none', title=bbi) + ylim(0,0.4) + xlim(-1,18) +
  labs(title="Ten Thousand 8x8 Smart Walks [Model]") +
  xlab("Successes") + ylab("Probability")