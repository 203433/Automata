import tkinter as tk
from getData import getDeclarations
from getData import getReservados
from getData import getPracticas
from automata.fa.dfa import DFA
# DFA which matches all binary strings ending in an odd number of '1's
dfa = DFA(
    allow_partial = True,
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20'},
    input_symbols={'1', '2' , '3', '4', '5', '6', '7', '8', '9', '0', '_',  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'},
    transitions={
        'q0': {'_': 'q1', 'a': 'q1', 'b': 'q1', 'c': 'q1', 'd': 'q1', 'e': 'q1', 'f': 'q1', 'g': 'q1', 'h': 'q1', 'i': 'q1', 'j': 'q1', 'k': 'q1', 'l': 'q1', 'm': 'q1', 'n': 'q1', 'o': 'q1', 'p': 'q1', 'q': 'q1', 'r': 'q1', 's': 'q1', 't': 'q1', 'u': 'q1', 'v': 'q1', 'w': 'q1', 'x': 'q1', 'y': 'q1', 'z': 'q1'},
        'q1': {'_': 'q2', 'a': 'q2', 'b': 'q2', 'c': 'q2', 'd': 'q2', 'e': 'q2', 'f': 'q2', 'g': 'q2', 'h': 'q2', 'i': 'q2', 'j': 'q2', 'k': 'q2', 'l': 'q2', 'm': 'q2', 'n': 'q2', 'o': 'q2', 'p': 'q2', 'q': 'q2', 'r': 'q2', 's': 'q2', 't': 'q2', 'u': 'q2', 'v': 'q2', 'w': 'q2', 'x': 'q2', 'y': 'q2', 'z': 'q2', 'A': 'q2', 'B': 'q2', 'C': 'q2', 'D': 'q2', 'E': 'q2', 'F': 'q2', 'G': 'q2', 'H': 'q2', 'I': 'q2', 'J': 'q2', 'K': 'q2', 'L': 'q2', 'M': 'q2', 'N': 'q2', 'O': 'q2', 'P': 'q2', 'Q': 'q2', 'R': 'q2', 'S': 'q2', 'T': 'q2', 'U': 'q2', 'V': 'q2', 'W': 'q2', 'X': 'q2', 'Y': 'q2', 'Z': 'q2', '0': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2'},
        'q2': {'_': 'q3', 'a': 'q3', 'b': 'q3', 'c': 'q3', 'd': 'q3', 'e': 'q3', 'f': 'q3', 'g': 'q3', 'h': 'q3', 'i': 'q3', 'j': 'q3', 'k': 'q3', 'l': 'q3', 'm': 'q3', 'n': 'q3', 'o': 'q3', 'p': 'q3', 'q': 'q3', 'r': 'q3', 's': 'q3', 't': 'q3', 'u': 'q3', 'v': 'q3', 'w': 'q3', 'x': 'q3', 'y': 'q3', 'z': 'q3', 'A': 'q3', 'B': 'q3', 'C': 'q3', 'D': 'q3', 'E': 'q3', 'F': 'q3', 'G': 'q3', 'H': 'q3', 'I': 'q3', 'J': 'q3', 'K': 'q3', 'L': 'q3', 'M': 'q3', 'N': 'q3', 'O': 'q3', 'P': 'q3', 'Q': 'q3', 'R': 'q3', 'S': 'q3', 'T': 'q3', 'U': 'q3', 'V': 'q3', 'W': 'q3', 'X': 'q3', 'Y': 'q3', 'Z': 'q3', '0': 'q3', '1': 'q3', '2': 'q3', '3': 'q3', '4': 'q3', '5': 'q3', '6': 'q3', '7': 'q3', '8': 'q3', '9': 'q3'},
        'q3': {'_': 'q4', 'a': 'q4', 'b': 'q4', 'c': 'q4', 'd': 'q4', 'e': 'q4', 'f': 'q4', 'g': 'q4', 'h': 'q4', 'i': 'q4', 'j': 'q4', 'k': 'q4', 'l': 'q4', 'm': 'q4', 'n': 'q4', 'o': 'q4', 'p': 'q4', 'q': 'q4', 'r': 'q4', 's': 'q4', 't': 'q4', 'u': 'q4', 'v': 'q4', 'w': 'q4', 'x': 'q4', 'y': 'q4', 'z': 'q4', 'A': 'q4', 'B': 'q4', 'C': 'q4', 'D': 'q4', 'E': 'q4', 'F': 'q4', 'G': 'q4', 'H': 'q4', 'I': 'q4', 'J': 'q4', 'K': 'q4', 'L': 'q4', 'M': 'q4', 'N': 'q4', 'O': 'q4', 'P': 'q4', 'Q': 'q4', 'R': 'q4', 'S': 'q4', 'T': 'q4', 'U': 'q4', 'V': 'q4', 'W': 'q4', 'X': 'q4', 'Y': 'q4', 'Z': 'q4', '0': 'q4', '1': 'q4', '2': 'q4', '3': 'q4', '4': 'q4', '5': 'q4', '6': 'q4', '7': 'q4', '8': 'q4', '9': 'q4'},
        'q4': {'_': 'q5', 'a': 'q5', 'b': 'q5', 'c': 'q5', 'd': 'q5', 'e': 'q5', 'f': 'q5', 'g': 'q5', 'h': 'q5', 'i': 'q5', 'j': 'q5', 'k': 'q5', 'l': 'q5', 'm': 'q5', 'n': 'q5', 'o': 'q5', 'p': 'q5', 'q': 'q5', 'r': 'q5', 's': 'q5', 't': 'q5', 'u': 'q5', 'v': 'q5', 'w': 'q5', 'x': 'q5', 'y': 'q5', 'z': 'q5', 'A': 'q5', 'B': 'q5', 'C': 'q5', 'D': 'q5', 'E': 'q5', 'F': 'q5', 'G': 'q5', 'H': 'q5', 'I': 'q5', 'J': 'q5', 'K': 'q5', 'L': 'q5', 'M': 'q5', 'N': 'q5', 'O': 'q5', 'P': 'q5', 'Q': 'q5', 'R': 'q5', 'S': 'q5', 'T': 'q5', 'U': 'q5', 'V': 'q5', 'W': 'q5', 'X': 'q5', 'Y': 'q5', 'Z': 'q5', '0': 'q5', '1': 'q5', '2': 'q5', '3': 'q5', '4': 'q5', '5': 'q5', '6': 'q5', '7': 'q5', '8': 'q5', '9': 'q5'},
        'q5': {'_': 'q6', 'a': 'q6', 'b': 'q6', 'c': 'q6', 'd': 'q6', 'e': 'q6', 'f': 'q6', 'g': 'q6', 'h': 'q6', 'i': 'q6', 'j': 'q6', 'k': 'q6', 'l': 'q6', 'm': 'q6', 'n': 'q6', 'o': 'q6', 'p': 'q6', 'q': 'q6', 'r': 'q6', 's': 'q6', 't': 'q6', 'u': 'q6', 'v': 'q6', 'w': 'q6', 'x': 'q6', 'y': 'q6', 'z': 'q6', 'A': 'q6', 'B': 'q6', 'C': 'q6', 'D': 'q6', 'E': 'q6', 'F': 'q6', 'G': 'q6', 'H': 'q6', 'I': 'q6', 'J': 'q6', 'K': 'q6', 'L': 'q6', 'M': 'q6', 'N': 'q6', 'O': 'q6', 'P': 'q6', 'Q': 'q6', 'R': 'q6', 'S': 'q6', 'T': 'q6', 'U': 'q6', 'V': 'q6', 'W': 'q6', 'X': 'q6', 'Y': 'q6', 'Z': 'q6', '0': 'q6', '1': 'q6', '2': 'q6', '3': 'q6', '4': 'q6', '5': 'q6', '6': 'q6', '7': 'q6', '8': 'q6', '9': 'q6'},
        'q6': {'_': 'q7', 'a': 'q7', 'b': 'q7', 'c': 'q7', 'd': 'q7', 'e': 'q7', 'f': 'q7', 'g': 'q7', 'h': 'q7', 'i': 'q7', 'j': 'q7', 'k': 'q7', 'l': 'q7', 'm': 'q7', 'n': 'q7', 'o': 'q7', 'p': 'q7', 'q': 'q7', 'r': 'q7', 's': 'q7', 't': 'q7', 'u': 'q7', 'v': 'q7', 'w': 'q7', 'x': 'q7', 'y': 'q7', 'z': 'q7', 'A': 'q7', 'B': 'q7', 'C': 'q7', 'D': 'q7', 'E': 'q7', 'F': 'q7', 'G': 'q7', 'H': 'q7', 'I': 'q7', 'J': 'q7', 'K': 'q7', 'L': 'q7', 'M': 'q7', 'N': 'q7', 'O': 'q7', 'P': 'q7', 'Q': 'q7', 'R': 'q7', 'S': 'q7', 'T': 'q7', 'U': 'q7', 'V': 'q7', 'W': 'q7', 'X': 'q7', 'Y': 'q7', 'Z': 'q7', '0': 'q7', '1': 'q7', '2': 'q7', '3': 'q7', '4': 'q7', '5': 'q7', '6': 'q7', '7': 'q7', '8': 'q7', '9': 'q7'},
        'q7': {'_': 'q8', 'a': 'q8', 'b': 'q8', 'c': 'q8', 'd': 'q8', 'e': 'q8', 'f': 'q8', 'g': 'q8', 'h': 'q8', 'i': 'q8', 'j': 'q8', 'k': 'q8', 'l': 'q8', 'm': 'q8', 'n': 'q8', 'o': 'q8', 'p': 'q8', 'q': 'q8', 'r': 'q8', 's': 'q8', 't': 'q8', 'u': 'q8', 'v': 'q8', 'w': 'q8', 'x': 'q8', 'y': 'q8', 'z': 'q8', 'A': 'q8', 'B': 'q8', 'C': 'q8', 'D': 'q8', 'E': 'q8', 'F': 'q8', 'G': 'q8', 'H': 'q8', 'I': 'q8', 'J': 'q8', 'K': 'q8', 'L': 'q8', 'M': 'q8', 'N': 'q8', 'O': 'q8', 'P': 'q8', 'Q': 'q8', 'R': 'q8', 'S': 'q8', 'T': 'q8', 'U': 'q8', 'V': 'q8', 'W': 'q8', 'X': 'q8', 'Y': 'q8', 'Z': 'q8', '0': 'q8', '1': 'q8', '2': 'q8', '3': 'q8', '4': 'q8', '5': 'q8', '6': 'q8', '7': 'q8', '8': 'q8', '9': 'q8'},
        'q8': {'_': 'q9', 'a': 'q9', 'b': 'q9', 'c': 'q9', 'd': 'q9', 'e': 'q9', 'f': 'q9', 'g': 'q9', 'h': 'q9', 'i': 'q9', 'j': 'q9', 'k': 'q9', 'l': 'q9', 'm': 'q9', 'n': 'q9', 'o': 'q9', 'p': 'q9', 'q': 'q9', 'r': 'q9', 's': 'q9', 't': 'q9', 'u': 'q9', 'v': 'q9', 'w': 'q9', 'x': 'q9', 'y': 'q9', 'z': 'q9', 'A': 'q9', 'B': 'q9', 'C': 'q9', 'D': 'q9', 'E': 'q9', 'F': 'q9', 'G': 'q9', 'H': 'q9', 'I': 'q9', 'J': 'q9', 'K': 'q9', 'L': 'q9', 'M': 'q9', 'N': 'q9', 'O': 'q9', 'P': 'q9', 'Q': 'q9', 'R': 'q9', 'S': 'q9', 'T': 'q9', 'U': 'q9', 'V': 'q9', 'W': 'q9', 'X': 'q9', 'Y': 'q9', 'Z': 'q9', '0': 'q9', '1': 'q9', '2': 'q9', '3': 'q9', '4': 'q9', '5': 'q9', '6': 'q9', '7': 'q9', '8': 'q9', '9': 'q9'},
        'q9': {'_': 'q10', 'a': 'q10', 'b': 'q10', 'c': 'q10', 'd': 'q10', 'e': 'q10', 'f': 'q10', 'g': 'q10', 'h': 'q10', 'i': 'q10', 'j': 'q10', 'k': 'q10', 'l': 'q10', 'm': 'q10', 'n': 'q10', 'o': 'q10', 'p': 'q10', 'q': 'q10', 'r': 'q10', 's': 'q10', 't': 'q10', 'u': 'q10', 'v': 'q10', 'w': 'q10', 'x': 'q10', 'y': 'q10', 'z': 'q10', 'A': 'q10', 'B': 'q10', 'C': 'q10', 'D': 'q10', 'E': 'q10', 'F': 'q10', 'G': 'q10', 'H': 'q10', 'I': 'q10', 'J': 'q10', 'K': 'q10', 'L': 'q10', 'M': 'q10', 'N': 'q10', 'O': 'q10', 'P': 'q10', 'Q': 'q10', 'R': 'q10', 'S': 'q10', 'T': 'q10', 'U': 'q10', 'V': 'q10', 'W': 'q10', 'X': 'q10', 'Y': 'q10', 'Z': 'q10', '0': 'q10', '1': 'q10', '2': 'q10', '3': 'q10', '4': 'q10', '5': 'q10', '6': 'q10', '7': 'q10', '8': 'q10', '9': 'q10'},
        'q10': {'_': 'q11', 'a': 'q11', 'b': 'q11', 'c': 'q11', 'd': 'q11', 'e': 'q11', 'f': 'q11', 'g': 'q11', 'h': 'q11', 'i': 'q11', 'j': 'q11', 'k': 'q11', 'l': 'q11', 'm': 'q11', 'n': 'q11', 'o': 'q11', 'p': 'q11', 'q': 'q11', 'r': 'q11', 's': 'q11', 't': 'q11', 'u': 'q11', 'v': 'q11', 'w': 'q11', 'x': 'q11', 'y': 'q11', 'z': 'q11', 'A': 'q11', 'B': 'q11', 'C': 'q11', 'D': 'q11', 'E': 'q11', 'F': 'q11', 'G': 'q11', 'H': 'q11', 'I': 'q11', 'J': 'q11', 'K': 'q11', 'L': 'q11', 'M': 'q11', 'N': 'q11', 'O': 'q11', 'P': 'q11', 'Q': 'q11', 'R': 'q11', 'S': 'q11', 'T': 'q11', 'U': 'q11', 'V': 'q11', 'W': 'q11', 'X': 'q11', 'Y': 'q11', 'Z': 'q11', '0': 'q11', '1': 'q11', '2': 'q11', '3': 'q11', '4': 'q11', '5': 'q11', '6': 'q11', '7': 'q11', '8': 'q11', '9': 'q11'},
        'q11': {'_': 'q12', 'a': 'q12', 'b': 'q12', 'c': 'q12', 'd': 'q12', 'e': 'q12', 'f': 'q12', 'g': 'q12', 'h': 'q12', 'i': 'q12', 'j': 'q12', 'k': 'q12', 'l': 'q12', 'm': 'q12', 'n': 'q12', 'o': 'q12', 'p': 'q12', 'q': 'q12', 'r': 'q12', 's': 'q12', 't': 'q12', 'u': 'q12', 'v': 'q12', 'w': 'q12', 'x': 'q12', 'y': 'q12', 'z': 'q12', 'A': 'q12', 'B': 'q12', 'C': 'q12', 'D': 'q12', 'E': 'q12', 'F': 'q12', 'G': 'q12', 'H': 'q12', 'I': 'q12', 'J': 'q12', 'K': 'q12', 'L': 'q12', 'M': 'q12', 'N': 'q12', 'O': 'q12', 'P': 'q12', 'Q': 'q12', 'R': 'q12', 'S': 'q12', 'T': 'q12', 'U': 'q12', 'V': 'q12', 'W': 'q12', 'X': 'q12', 'Y': 'q12', 'Z': 'q12', '0': 'q12', '1': 'q12', '2': 'q12', '3': 'q12', '4': 'q12', '5': 'q12', '6': 'q12', '7': 'q12', '8': 'q12', '9': 'q12'},
        'q12': {'_': 'q13', 'a': 'q13', 'b': 'q13', 'c': 'q13', 'd': 'q13', 'e': 'q13', 'f': 'q13', 'g': 'q13', 'h': 'q13', 'i': 'q13', 'j': 'q13', 'k': 'q13', 'l': 'q13', 'm': 'q13', 'n': 'q13', 'o': 'q13', 'p': 'q13', 'q': 'q13', 'r': 'q13', 's': 'q13', 't': 'q13', 'u': 'q13', 'v': 'q13', 'w': 'q13', 'x': 'q13', 'y': 'q13', 'z': 'q13', 'A': 'q13', 'B': 'q13', 'C': 'q13', 'D': 'q13', 'E': 'q13', 'F': 'q13', 'G': 'q13', 'H': 'q13', 'I': 'q13', 'J': 'q13', 'K': 'q13', 'L': 'q13', 'M': 'q13', 'N': 'q13', 'O': 'q13', 'P': 'q13', 'Q': 'q13', 'R': 'q13', 'S': 'q13', 'T': 'q13', 'U': 'q13', 'V': 'q13', 'W': 'q13', 'X': 'q13', 'Y': 'q13', 'Z': 'q13', '0': 'q13', '1': 'q13', '2': 'q13', '3': 'q13', '4': 'q13', '5': 'q13', '6': 'q13', '7': 'q13', '8': 'q13', '9': 'q13'},
        'q13': {'_': 'q14', 'a': 'q14', 'b': 'q14', 'c': 'q14', 'd': 'q14', 'e': 'q14', 'f': 'q14', 'g': 'q14', 'h': 'q14', 'i': 'q14', 'j': 'q14', 'k': 'q14', 'l': 'q14', 'm': 'q14', 'n': 'q14', 'o': 'q14', 'p': 'q14', 'q': 'q14', 'r': 'q14', 's': 'q14', 't': 'q14', 'u': 'q14', 'v': 'q14', 'w': 'q14', 'x': 'q14', 'y': 'q14', 'z': 'q14', 'A': 'q14', 'B': 'q14', 'C': 'q14', 'D': 'q14', 'E': 'q14', 'F': 'q14', 'G': 'q14', 'H': 'q14', 'I': 'q14', 'J': 'q14', 'K': 'q14', 'L': 'q14', 'M': 'q14', 'N': 'q14', 'O': 'q14', 'P': 'q14', 'Q': 'q14', 'R': 'q14', 'S': 'q14', 'T': 'q14', 'U': 'q14', 'V': 'q14', 'W': 'q14', 'X': 'q14', 'Y': 'q14', 'Z': 'q14', '0': 'q14', '1': 'q14', '2': 'q14', '3': 'q14', '4': 'q14', '5': 'q14', '6': 'q14', '7': 'q14', '8': 'q14', '9': 'q14'},
        'q14': {'_': 'q15', 'a': 'q15', 'b': 'q15', 'c': 'q15', 'd': 'q15', 'e': 'q15', 'f': 'q15', 'g': 'q15', 'h': 'q15', 'i': 'q15', 'j': 'q15', 'k': 'q15', 'l': 'q15', 'm': 'q15', 'n': 'q15', 'o': 'q15', 'p': 'q15', 'q': 'q15', 'r': 'q15', 's': 'q15', 't': 'q15', 'u': 'q15', 'v': 'q15', 'w': 'q15', 'x': 'q15', 'y': 'q15', 'z': 'q15', 'A': 'q15', 'B': 'q15', 'C': 'q15', 'D': 'q15', 'E': 'q15', 'F': 'q15', 'G': 'q15', 'H': 'q15', 'I': 'q15', 'J': 'q15', 'K': 'q15', 'L': 'q15', 'M': 'q15', 'N': 'q15', 'O': 'q15', 'P': 'q15', 'Q': 'q15', 'R': 'q15', 'S': 'q15', 'T': 'q15', 'U': 'q15', 'V': 'q15', 'W': 'q15', 'X': 'q15', 'Y': 'q15', 'Z': 'q15', '0': 'q15', '1': 'q15', '2': 'q15', '3': 'q15', '4': 'q15', '5': 'q15', '6': 'q15', '7': 'q15', '8': 'q15', '9': 'q15'},
        'q15': {'_': 'q16', 'a': 'q16', 'b': 'q16', 'c': 'q16', 'd': 'q16', 'e': 'q16', 'f': 'q16', 'g': 'q16', 'h': 'q16', 'i': 'q16', 'j': 'q16', 'k': 'q16', 'l': 'q16', 'm': 'q16', 'n': 'q16', 'o': 'q16', 'p': 'q16', 'q': 'q16', 'r': 'q16', 's': 'q16', 't': 'q16', 'u': 'q16', 'v': 'q16', 'w': 'q16', 'x': 'q16', 'y': 'q16', 'z': 'q16', 'A': 'q16', 'B': 'q16', 'C': 'q16', 'D': 'q16', 'E': 'q16', 'F': 'q16', 'G': 'q16', 'H': 'q16', 'I': 'q16', 'J': 'q16', 'K': 'q16', 'L': 'q16', 'M': 'q16', 'N': 'q16', 'O': 'q16', 'P': 'q16', 'Q': 'q16', 'R': 'q16', 'S': 'q16', 'T': 'q16', 'U': 'q16', 'V': 'q16', 'W': 'q16', 'X': 'q16', 'Y': 'q16', 'Z': 'q16', '0': 'q16', '1': 'q16', '2': 'q16', '3': 'q16', '4': 'q16', '5': 'q16', '6': 'q16', '7': 'q16', '8': 'q16', '9': 'q16'},
        'q16': {'_': 'q17', 'a': 'q17', 'b': 'q17', 'c': 'q17', 'd': 'q17', 'e': 'q17', 'f': 'q17', 'g': 'q17', 'h': 'q17', 'i': 'q17', 'j': 'q17', 'k': 'q17', 'l': 'q17', 'm': 'q17', 'n': 'q17', 'o': 'q17', 'p': 'q17', 'q': 'q17', 'r': 'q17', 's': 'q17', 't': 'q17', 'u': 'q17', 'v': 'q17', 'w': 'q17', 'x': 'q17', 'y': 'q17', 'z': 'q17', 'A': 'q17', 'B': 'q17', 'C': 'q17', 'D': 'q17', 'E': 'q17', 'F': 'q17', 'G': 'q17', 'H': 'q17', 'I': 'q17', 'J': 'q17', 'K': 'q17', 'L': 'q17', 'M': 'q17', 'N': 'q17', 'O': 'q17', 'P': 'q17', 'Q': 'q17', 'R': 'q17', 'S': 'q17', 'T': 'q17', 'U': 'q17', 'V': 'q17', 'W': 'q17', 'X': 'q17', 'Y': 'q17', 'Z': 'q17', '0': 'q17', '1': 'q17', '2': 'q17', '3': 'q17', '4': 'q17', '5': 'q17', '6': 'q17', '7': 'q17', '8': 'q17', '9': 'q17'},
        'q17': {'_': 'q18', 'a': 'q18', 'b': 'q18', 'c': 'q18', 'd': 'q18', 'e': 'q18', 'f': 'q18', 'g': 'q18', 'h': 'q18', 'i': 'q18', 'j': 'q18', 'k': 'q18', 'l': 'q18', 'm': 'q18', 'n': 'q18', 'o': 'q18', 'p': 'q18', 'q': 'q18', 'r': 'q18', 's': 'q18', 't': 'q18', 'u': 'q18', 'v': 'q18', 'w': 'q18', 'x': 'q18', 'y': 'q18', 'z': 'q18', 'A': 'q18', 'B': 'q18', 'C': 'q18', 'D': 'q18', 'E': 'q18', 'F': 'q18', 'G': 'q18', 'H': 'q18', 'I': 'q18', 'J': 'q18', 'K': 'q18', 'L': 'q18', 'M': 'q18', 'N': 'q18', 'O': 'q18', 'P': 'q18', 'Q': 'q18', 'R': 'q18', 'S': 'q18', 'T': 'q18', 'U': 'q18', 'V': 'q18', 'W': 'q18', 'X': 'q18', 'Y': 'q18', 'Z': 'q18', '0': 'q18', '1': 'q18', '2': 'q18', '3': 'q18', '4': 'q18', '5': 'q18', '6': 'q18', '7': 'q18', '8': 'q18', '9': 'q18'},
        'q18': {'_': 'q19', 'a': 'q19', 'b': 'q19', 'c': 'q19', 'd': 'q19', 'e': 'q19', 'f': 'q19', 'g': 'q19', 'h': 'q19', 'i': 'q19', 'j': 'q19', 'k': 'q19', 'l': 'q19', 'm': 'q19', 'n': 'q19', 'o': 'q19', 'p': 'q19', 'q': 'q19', 'r': 'q19', 's': 'q19', 't': 'q19', 'u': 'q19', 'v': 'q19', 'w': 'q19', 'x': 'q19', 'y': 'q19', 'z': 'q19', 'A': 'q19', 'B': 'q19', 'C': 'q19', 'D': 'q19', 'E': 'q19', 'F': 'q19', 'G': 'q19', 'H': 'q19', 'I': 'q19', 'J': 'q19', 'K': 'q19', 'L': 'q19', 'M': 'q19', 'N': 'q19', 'O': 'q19', 'P': 'q19', 'Q': 'q19', 'R': 'q19', 'S': 'q19', 'T': 'q19', 'U': 'q19', 'V': 'q19', 'W': 'q19', 'X': 'q19', 'Y': 'q19', 'Z': 'q19', '0': 'q19', '1': 'q19', '2': 'q19', '3': 'q19', '4': 'q19', '5': 'q19', '6': 'q19', '7': 'q19', '8': 'q19', '9': 'q19'},
        'q19': {'_': 'q20', 'a': 'q20', 'b': 'q20', 'c': 'q20', 'd': 'q20', 'e': 'q20', 'f': 'q20', 'g': 'q20', 'h': 'q20', 'i': 'q20', 'j': 'q20', 'k': 'q20', 'l': 'q20', 'm': 'q20', 'n': 'q20', 'o': 'q20', 'p': 'q20', 'q': 'q20', 'r': 'q20', 's': 'q20', 't': 'q20', 'u': 'q20', 'v': 'q20', 'w': 'q20', 'x': 'q20', 'y': 'q20', 'z': 'q20', 'A': 'q20', 'B': 'q20', 'C': 'q20', 'D': 'q20', 'E': 'q20', 'F': 'q20', 'G': 'q20', 'H': 'q20', 'I': 'q20', 'J': 'q20', 'K': 'q20', 'L': 'q20', 'M': 'q20', 'N': 'q20', 'O': 'q20', 'P': 'q20', 'Q': 'q20', 'R': 'q20', 'S': 'q20', 'T': 'q20', 'U': 'q20', 'V': 'q20', 'W': 'q20', 'X': 'q20', 'Y': 'q20', 'Z': 'q20', '0': 'q20', '1': 'q20', '2': 'q20', '3': 'q20', '4': 'q20', '5': 'q20', '6': 'q20', '7': 'q20', '8': 'q20', '9': 'q20'},
        'q20': {}
    },
    initial_state='q0',
    final_states={'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19','q20'}
)
def pruebas():
    root = tk.Tk()
    T = tk.Text(root, height=100, width=150, bg="black", fg="white", font=("Arial", 12, "bold"))
    T.pack()
    T.insert(tk.END,"Se debe seguir la estructura int variable; o int variable = 0; donde int puede ser cualquier tipo basico y variable puede ser cualquier palabra, para ser considerada dentro del programa debe terminar con ; \n" )
    T.insert(tk.END,"Una declaracion para ser considerada correcta debe cumplir con las reglas establecidas en el automata y no caer dentro de una palabra reservada, el apartado de mejores practicas es para buscar las mejores formas de declarar variables, tomando en cuenta su longitud y las palabras utilizadas \n" )
    T.insert(tk.END,"----------------------------------------- \n " )
    for c in getDeclarations():
        if dfa.accepts_input(c):
            print(c + ' cumple con las reglas establecidas')
            T.insert(tk.END, c + " sigue todas las reglas establecidas \n" )
            
        else:
            print(c + ' no cumple con las reglas establecidas')
            T.insert(tk.END, c + " No sigue todas las reglas establecidas \n" )

        for x in getReservados():
            if c == x:
                print(c + ' es una palabra reservada')
                T.insert(tk.END, c + ' es una palabra reservada \n' )   
        print("Las mejores practicas para la declaracion de " + c + " son:")
        T.insert(tk.END, "Las mejores practicas para la declaracion de " + c + " son: \n" )
        for x in getPracticas():
            if len(c) == len(x):
                T.insert(tk.END,  x + '\n')    
                print(x )   
        T.insert(tk.END,"----------------------------------------- \n " )

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("500x500")
    ventana.title("Analizador de Declaraciones")
    tk.Button(
        ventana,
        pady=10,
        text="Seleccionar archivo txt",
        fg="black",
        bg="white",
        justify="center",
        command=pruebas,
    ).pack(
        side="top",
    )
    ventana.mainloop()