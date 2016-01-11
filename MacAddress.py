import sys



hex_bin_dict = {"0":"0000",
                "1":"0001",
                "2":"0010",
                "3":"0011",
                "4":"0100",
                "5":"0101",
                "6":"0110",
                "7":"0111",
                "8":"1000",
                "9":"1001",
                "A":"1010",
                "B":"1011",
                "C":"1100",
                "D":"1101",
                "E":"1110",
                "F":"1111"}

if __name__ == "__main__":
    mac_address_str = sys.argv[1]

    digits = mac_address_str.split(':')
    bin_rep_list = []
    for d in digits:
        bin_rep_list.append(hex_bin_dict[d[0]])
        bin_rep_list.append(hex_bin_dict[d[1]])

    print(mac_address_str, "->", ''.join(bin_rep_list))
