class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init
        loss = init ** 2
        for _ in range(iterations):
            
            # current value of loss
            loss = x ** 2
            # derivative
            d = 2 * x

            # update rule
            x = x - learning_rate * d

        return round(x, 5)


