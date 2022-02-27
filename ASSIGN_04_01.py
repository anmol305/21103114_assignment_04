# Tower of hanoi problem
# source is where all the disc are kept initially
# helper is the rod used to transfer disc
# destination is where all the disc finally be placed
def hanoi_tower(n, source, helper, destination):
    if n == 1:
        print(f"move disc 1 from {source} to {destination}")
        return
    hanoi_tower(n - 1, source=source, helper=destination, destination=helper)
    print(f"move {n} disc from {source} to {destination}")
    hanoi_tower(n - 1, source=helper, helper=source, destination=destination)


n = int(input("Enter the number of discs: "))
hanoi_tower(n, "A", "B", "C")
