x = 10

def func() -> None:
    global x
    x = 5
    print(x)

if __name__ == "__main__":
    print(f"In main (1), x = {x}")
    func()
    print(f"In main (2), x = {x}")
