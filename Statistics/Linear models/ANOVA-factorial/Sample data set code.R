# Code for making random factorial data set
```{r, echo=FALSE}
set.seed(10)
Richness = sort(round(rnorm(60,mean=60,sd=10)))
HighVert = sample(Richness[1:10])
HighHor = sample(Richness[11:20])
LowVert = sample(Richness[31:40])
LowHor = sample(Richness[21:30])
NoneVert = sample(Richness[c(41:45,51:55)])
NoneHor = sample(Richness[c(46:50,56:60)])
Richness = c(NoneVert,NoneHor,LowVert,LowHor,HighVert,HighHor)
Copper = rep(c("None","Low","High"),each=20)
Orientation = rep(c("vertical","Horizontal"),each=10,times=3)
Sessile = data.frame(cbind(Richness,Copper,Orientation))
Sessile$Richness = as.integer(as.character((Sessile$Richness)))
write.csv(Sessile, "Sessile.csv", row.names=FALSE)
```
