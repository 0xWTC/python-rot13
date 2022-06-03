# ROT13 coder and decoder

def rot13(text):
    """
    ROT13 coder and decoder
    """
    rot13_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                rot13_text += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                rot13_text += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            rot13_text += char
    return rot13_text

def reverse_rot13(text):
    """
    Reverse ROT13 coder and decoder
    """
    rot13_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                rot13_text += chr((ord(char) - ord('A') - 13) % 26 + ord('A'))
            else:
                rot13_text += chr((ord(char) - ord('a') - 13) % 26 + ord('a'))
        else:
            rot13_text += char
    return rot13_text

def main(text):
    """
    Main function
    """
    result = rot13(text)
    print("ROT13:", result)
    reverse = reverse_rot13(result)
    print("Reversed:", reverse)

def test():
    """
    Test function
    """
    assert rot13("Nofheqvfz vf gur cuvybfbcuvpny gurfvf gung yvsr, be gur jbeyq va trareny, vf nofheq.") == "Absurdism is the philosophical thesis that life, or the world in general, is absurd."
    assert rot13("Inevbhf cbchyne nethzragf ner bsgra pvgrq va snibe bs nofheqvfz.") == "Various popular arguments are often cited in favor of absurdism."
    assert rot13("Nabgure nethzrag cebprrqf vaqverpgyl ol cbvagvat bhg ubj inevbhf terng guvaxref unir boivbhf veengvbany ryrzragf va gurve flfgrzf bs gubhtug.") == "Another argument proceeds indirectly by pointing out how various great thinkers have obvious irrational elements in their systems of thought."

    print("All tests passed!")
    print("="*50)

if __name__ == "__main__":
    test()
    main("The most common criticism of absurdism is to argue that life in fact has meaning.")
