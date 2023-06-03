def phoneNumberMnemonics(phoneNumber):
    keypad = {
        "0": ["0"],
        "1": ["1"],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"],
    }
    
    results = [""]

    for number in phoneNumber:
        next_results = [existing + char for existing in results for char in keypad[number]]
        results = next_results
    return results

phone_number = "1905"
print(phoneNumberMnemonics(phoneNumber=phone_number))