def bayes_theorem(prior_a, prior_b, conditional_b_given_a):
    # P(A|B) = (P(B|A) * P(A)) / P(B)
    posterior_a_given_b = (conditional_b_given_a * prior_a) / prior_b
    return posterior_a_given_b

# Example usage:
prior_a = 0.3
prior_b = 0.6
conditional_b_given_a = 0.8
print(bayes_theorem(prior_a, prior_b, conditional_b_given_a))
# Output: 0.4
