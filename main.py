from Flatmate_Classes import Bill, Flatmate
from Report_Class import PDFReport

if __name__ == '__main__':
    print()
    bill_amount = float(input('Enter the total bill amount: '))

    print()
    bill_period = input('Please enter the bill period (e.g. June 2023): ')

    curr_bill = Bill(amount=bill_amount, period=bill_period)

    add_flatmates = 'Y'
    flatmates = []
    while add_flatmates.upper() == 'Y':
        print()
        flatmate_name = input('Please enter the name of the flatmate: ')

        print()
        flatmate_days_in_house = int(input(f'Please enter the number of days {flatmate_name} stayed in the house for the bill period: '))
        new_flatmate = Flatmate(name=flatmate_name.title(), days_in_house=flatmate_days_in_house)
        flatmates.append(new_flatmate)

        print()
        add_flatmates = input('Do you want to add more flatmates? (Enter Y/N): ')

    # flatmate1 = Flatmate(name='Shashank', days_in_house=15)
    # flatmate2 = Flatmate(name='Neha', days_in_house=20)
    # flatmate3 = Flatmate(name='Tavishq', days_in_house=10)
    # flatmate4 = Flatmate(name='Kusum', days_in_house=30)

    # print(f'Shashank pays: {flatmate1.pays(bill=curr_bill, other_flat_mates=[flatmate2, flatmate3, flatmate4])}')
    # print(f'Neha pays: {flatmate2.pays(bill=curr_bill, other_flat_mates=[flatmate1, flatmate3, flatmate4])}')
    # print(f'Tavishq pays: {flatmate3.pays(bill=curr_bill, other_flat_mates=[flatmate1, flatmate2, flatmate4])}')
    # print(f'Kusum pays: {flatmate4.pays(bill=curr_bill, other_flat_mates=[flatmate1, flatmate2, flatmate3])}')

    pdf = PDFReport(f'Reports\\Bill - {curr_bill.period}.pdf')
    pdf.pdf_generator(flatmates, curr_bill)
