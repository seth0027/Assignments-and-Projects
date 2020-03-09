# # Problem Set 4A
# # Name: <your name here>
# # Collaborators:
# # Time Spent: x:xx


def get_permutations(sequence):
    #     '''
    #     Enumerate all permutations of a given string

    #     sequence (string): an arbitrary string to permute. Assume that it is a
    #     non-empty string.

    #     You MUST use recursion for this part. Non-recursive solutions will not be
    #     accepted.

    #     Returns: a list of all permutations of sequence

    #     Example:
    #     >>> get_permutations('abc')
    #     ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    #     Note: depending on your implementation, you may return the permutations in
    #     a different order than what is listed here.
    #     '''

    if len(sequence) == 1:
        return [sequence]

    else:
        li = []
        for i in range(0, len(sequence)):
            letter = sequence[i]
            remaining = sequence[:i] + sequence[i+1:]
            for perm in get_permutations(remaining):
                li.append(letter+perm)
        return li
#         return get_permutations(sequence[0])+get_permutations(sequence[1:])


if __name__ == '__main__':
    #     # EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

# #    # Put three example test cases here (for your sanity, limit your inputs
# #    to be three characters or fewer as you will have n! permutations for a
# #    sequence of length n)

#     pass  # delete this line and replace with your code here


# def build_shift_dict(shift):
#     '''
#     Creates a dictionary that can be used to apply a cipher to a letter.
#     The dictionary maps every uppercase and lowercase letter to a
#     character shifted down the alphabet by the input shift. The dictionary
#     should have 52 keys of all the uppercase letters and all the lowercase
#     letters only.

#     shift (integer): the amount by which to shift every letter of the
#     alphabet. 0 <= shift < 26

#     Returns: a dictionary mapping a letter (string) to
#              another letter (string).
#     '''
#     letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
#     dicti = {}

#     for char in letters:
#         dicti[char] = chr(ord(char)+shift % 26)

#     return dicti


# print(build_shift_dict(2))
