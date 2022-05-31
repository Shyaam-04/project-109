import plotly.figure_factory as ff
import statistics
import pandas as pd

df = pd.read_csv("data_109P.csv")
data = df["reading score"].tolist()

mean = statistics.mean(data)
med = statistics.median(data)
mode = statistics.mode(data)
sd = statistics.stdev(data)
print("Mean of this data is "+str(mean))
print("Median of this data is "+str(med))
print("Mode of this data is "+str(mode))
print("Standard deviation of this data is "+str(sd))

f_sd_st,f_sd_e = mean-sd,mean+sd
s_sd_st,s_sd_e = mean-(2*sd),mean+(2*sd)
t_sd_st,t_sd_e = mean-(3*sd),mean+(3*sd)

f_sd = [result for result in data if result>f_sd_st and result<f_sd_e]
s_sd = [result for result in data if result>s_sd_st and result<s_sd_e]
t_sd = [result for result in data if result>t_sd_st and result<t_sd_e]

per1 = (len(f_sd)/len(data))*100
per2 = (len(s_sd)/len(data))*100
per3 = (len(t_sd)/len(data))*100

print(str(per1)+"% of data lies within 1 standard deviation")
print(str(per2)+"% of data lies within 2 standard deviation")
print(str(per3)+"% of data lies within 3 standard deviation")