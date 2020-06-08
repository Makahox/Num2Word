num2words1 = {0: "Zero", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def number(Number):
    if 0 <= Number <= 19:
        print(num2words1[Number])
    elif 20 <= Number <= 99:
        tens, remainder = divmod(Number, 10)
        print(num2words2[tens - 2] + "-" + num2words1[remainder] if remainder else num2words2[tens -2])
    else:
        print("That number is outside of the available range")
        return False


def main():
    while True:
        try:
            num = int(input("Please enter a number between 0 and 99: "))
            if number(num) == False:
                continue
        except ValueError:
            print("that is an invalid number")
            continue
        else:
            break
main()
