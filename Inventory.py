import sys



if __name__ == "__main__":
    with open(sys.argv[1], "r") as inventory_file:

        # total = 0.0
        # for line in inventory_file:
        #     item, quantity, price = line.split()
        #     total += int(quantity) * float(price)
        #
        # print("Total price = {:6.2f}".format(total))
        #

        print(sum([int(line.split()[1]) * float(line.split()[2]) for line in inventory_file]))