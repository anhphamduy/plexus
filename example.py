from plexus import Stack, Human, StackSearcher

n_levels = int(input("How many levels in the water stack? "))
stack = Stack(n_levels=n_levels)

human = Human()
searcher = StackSearcher()

while True:
    water_amount = float(input("How much water are you pouring? "))

    human.pour(stack, water_amount)

    i = int(input("i position of your glass: "))
    j = int(input("j position of your glass: "))
    print("Result", searcher.search_glass(stack, i, j))
