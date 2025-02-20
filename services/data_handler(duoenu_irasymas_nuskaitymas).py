import pickle

def load_file():
    try:
        with open("budget.pickle", "rb") as file:
            budget = pickle.load(file)
        return budget
    except FileNotFoundError:
        return Budget()


def save_file(budget):
    with open("budget.pickle", "wb") as file:
        pickle.dump(budget, file)