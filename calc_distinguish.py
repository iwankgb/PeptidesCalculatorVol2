"""prevent error when standard amino sequence is the same as non standard e.g ooo(ooo)ooo(ooo),
by adding * to non standard amino"""


class Distinguish:

    def distinguish_non_standard(self, data_sequence):
        substr = ")"
        distinguishing_sign = "*"
        return (distinguishing_sign + substr).join(data_sequence.split(substr))
