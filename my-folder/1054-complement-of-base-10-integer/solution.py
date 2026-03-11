class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # bit ^ 1 will flip it
        # make a master bit 11...111 (bit length)

        master = (1 << n.bit_length()) - 1
        return n ^ master if n != 0 else 1
