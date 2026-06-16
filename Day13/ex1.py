from numpy import positive
def bayes_throrm(prior,sensitivity,specificity):
    evidence = (sensitivity*prior)+((1-sensitivity)*(1-prior))
    posterior = (sensitivity *prior)/evidence
    return posterior 
prior =0.01#1 % preevalence 
sensitivity =0.95 # True positive rate 
specificity = 0.9 # True negative rate

posterior = bayes_throrm(prior,sensitivity,specificity)
print("Probability of having the disease after testing positive is : {0:.2f}%".format(posterior*100))