def convert_packet(packet):
    pkt_int = int(packet, base=16)
    pkt_bin = bin(int(packet, base=16))
    return pkt_int, pkt_bin

def parse_header_and_body(packet):
    pkt_ver = int(packet[0:3], base=2)
    pkt_type_id = int(packet[3:6], base=2)
    return pkt_ver, pkt_type_id, packet[6:]

def process_literal(pkt_body):
    result = ""
    counter = 0
    prefix = 1
    # can loop through whole list or slice out prefixes until a 0 is encountered, then chop off the trailing bits
    # for b in pkt_body:
    #     if counter == 0:
    #         prefix = int(b, base=2)
    #     else:
    #         result += b
    #     if counter < 4:
    #         counter += 1
    #     else:
    #         counter = 0
    #         if prefix == 0:
    #             break
    
    pfx_pointer = 0
    while prefix:
        prefix = int(pkt_body[pfx_pointer], base=2)
        result += pkt_body[pfx_pointer + 1:pfx_pointer + 5]
        pfx_pointer += 5

        

    print(result)
    print(int(result,base=2))


def process_packet(packet):
    pkt_ver, pkt_type_id, pkt_body = parse_header_and_body(packet)
    if pkt_type_id == 4:
        process_literal(pkt_body)

packet_types = ["","","","","literal"]
    
def main():
    with open("small.txt", "r") as input:
        pkt_int, pkt_bin = convert_packet(input.readline())
    process_packet(pkt_bin[2:])

if __name__ == "__main__":
    main()