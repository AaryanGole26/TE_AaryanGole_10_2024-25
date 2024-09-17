# Define function for Bayes' Theorem
def bayesTheorem(pA, pB, pBA):
    return pA * pBA / pB

# Prompt user to input probabilities
pRain = float(input("Enter the prior probability of rain (P(Rain)): "))
pCloudy = float(input("Enter the probability of it being cloudy (P(Cloudy)): "))
pCloudyRain = float(input("Enter the probability of cloudy given rain (P(Cloudy|Rain)): "))

# Use function to calculate conditional probability
posterior_probability = bayesTheorem(pRain, pCloudy, pCloudyRain)

# Display result
print(f"The conditional probability P(Rain|Cloudy) is: {posterior_probability:.4f}")

''' 
Output : 
 Enter the prior probability of rain (P(Rain)): 0.2
 Enter the probability of it being cloudy (P(Cloudy)): 0.4
 Enter the probability of cloudy given rain (P(Cloudy|Rain)): 0.85
 The conditional probability P(Rain|Cloudy) is: 0.4250
'''
