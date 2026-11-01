class StockSpanner:

    def __init__(self):
        self.prices = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.prices and self.prices[-1][0] <= price:
            _, add = self.prices.pop()
            span += add

        self.prices.append((price, span))
        return span

        


