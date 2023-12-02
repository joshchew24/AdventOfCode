import sys


def convert_packet(packet):
    expected_bin_length = len(packet)*4
    pkt_int = int(packet, base=16)
    pkt_bin = bin(int(packet, base=16))[2:]
    diff = expected_bin_length - len(pkt_bin)
    while diff:
        pkt_bin = "0" + pkt_bin
        diff -= 1
    return pkt_int, pkt_bin

def parse_header_and_body(packet):
    # breakpoint()
    pkt_ver = int(packet[0:3], base=2)
    pkt_type_id = int(packet[3:6], base=2)
    return pkt_ver, pkt_type_id, packet[6:]

# returns value of literal and final index of literal chunk
def process_literal(pkt_body):
    result = ""
    prefix = 1
    
    pfx_pointer = 0
    while prefix:
        breakpoint()
        prefix = int(pkt_body[pfx_pointer], base=2)
        result += pkt_body[pfx_pointer + 1:pfx_pointer + 5]
        pfx_pointer += 5

    return result, 5 + pfx_pointer

def process_operands(pkt_body):
    # breakpoint()
    pkt_len_id = int(pkt_body[0])
    sub_pkts_ver_sum = 0
    total_end_idx = 0
    if pkt_len_id: # packet-wise length
        breakpoint()
        pkt_count = int(pkt_body[1:12], base=2)
        sub_packets = pkt_body[12:]
        while pkt_count > 0:
            breakpoint()
            ver_sum, end_idx = process_packet(sub_packets)
            sub_packets = sub_packets[end_idx + 1:]
            sub_pkts_ver_sum += ver_sum
            total_end_idx += end_idx
            pkt_count -= 1
    else: # bit-wise length
        bit_count = int(pkt_body[1:16], base=2)
        sub_packets = pkt_body[16:]
        while bit_count > 0:
            ver_sum, end_idx = process_packet(sub_packets)
            # breakpoint()
            sub_packets = sub_packets[end_idx + 1:]
            sub_pkts_ver_sum += ver_sum
            total_end_idx += end_idx
            bit_count -= end_idx + 1
    return sub_pkts_ver_sum, end_idx

# return sum of version numbers in packet and subpackets
def process_packet(packet):
    # breakpoint()
    pkt_ver, pkt_type_id, pkt_body = parse_header_and_body(packet)

    sum = pkt_ver
    end_idx = len(packet) - 1

    if pkt_type_id == 4:
        literal_value, end_idx = process_literal(pkt_body)
    else:
        operands_sum, end_idx = process_operands(pkt_body)
        sum += operands_sum
    return sum, end_idx

packet_types = ["","","","","literal"]
    
inputs = ["input", "small", "bit_length", "pkt_length", "nested", "tree_same", "tree_diff", "nested_big"]
def main():
    input_idx = int(sys.argv[1])
    with open(inputs[input_idx] + ".txt", "r") as input:
        pkt_int, pkt_bin = convert_packet(input.readline())
    print(pkt_bin)
    print(process_packet(pkt_bin))

if __name__ == "__main__":
    main()