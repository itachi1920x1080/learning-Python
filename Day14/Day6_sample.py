# from numpy import median
# from statistics import mode
# # mean
# data = [10,20,30,40]
# mean = sum(data)/len(data)
# print("mean : ",mean)

# # median
# sorted_data = sorted(data)
# # print("sorted_data : ",sorted_data)
# median = sorted_data [len(data)//2]if len(data)%2!=0 else (sorted_data[len(data)//2 -1 ]+sorted_data[len(data)//2])/2
# print("median : ",median)
# print("mode : ",mode(data))

# variance = sum ((x -mean)**2 for x in data )/len (data)
# print("Variance : ",variance)
# std_dev = variance ** 0.5
# print ("standardDeviation : ",std_dev)

# pyrefly: ignore [missing-import]
import  scipy.stats as stats


data = [10,20,30,40,50]

mean = sum (data)/len (data)
sample_mean = mean
variance = sum ((x -mean)**2 for x in data )/len (data)
std_dev = variance ** 0.5
z_score =1.96
confidence_interval= (sample_mean-z_score*(std_dev /len(data)**0.5),sample_mean+z_score*(std_dev /len(data)**0.5))
print("mean : ",mean)
print("sample_mean : ",sample_mean)
print("variance : ",variance)
print("std_dev : ",std_dev)
print("z_score : ",z_score)
print("confidence_interval : ",confidence_interval)




