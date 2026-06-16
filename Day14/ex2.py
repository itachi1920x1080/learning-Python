from scipy.stats import ttest_ind

group1 =[2.1,2.5,2.8,3.0,3.2] 
group2 = [2.0,2.4,2.7,3.0,3.0] 

t_stat , p_value = ttest_ind(group1,group2)
print("T-statistics: ",t_stat)
print("P-value: ",p_value)


alpha = 0.05
if p_value < alpha:
    print("Reject the null hyposthesi : siginificant difference") 
else:
    print("Fail to reject the null hypothesis : NO siginificant diffrence") 