#   ------------------------------------#
#   Title: Mailroom Part 1
#   Dev: SChang
#   Date: Feb 2nd, 2019
#   ChangeLog: (Who, When, What)
#   SChang,02/02/2019, Created Script
#   ------------------------------------#

import sys

# a list of all donars that is loaded
donor_list = [('William Gates', [1010, 2020, 3030]),
              ('Mark Zuckerberg', [5500, 4400]),
              ('Jeff Bezos', [6745, 2345, 3845]),
              ('Paul Allen', [9999, 8888, 7777])]


# menu prompt for options
prompt_menu = "\n".join(("",
          "Charity Management Application",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))


# function for sending thank you or adding new donor
def send_ty():
    while True:
        DonorName = input("""Provide Donor Full Name, or type: "List" to display a list of all donors: """).strip()
        DonorName = DonorName.title()
# if statement for either listing donors or adding new donor if not found in list
        if DonorName == "List":
            view_donors()
            NewDonor = DonorName

        elif DonorName not in donor_list:
            NewDonor = (DonorName, [])
            donor_list.append(NewDonor)
            donation_amount = float(input("Enter donation amount: "))
            NewDonor[-1].append(donation_amount)
            print("Thank you, {} for donating ${:.2f}".format(DonorName, donation_amount))
            break


# viewing list of donors if "List" is entered from menu
def view_donors():
    for donor in donor_list:
        print(donor[0])


def report_sort(item):
    return item[1]


# function for report that is formatted with donor information
def create_report ():
    print()
    print("{:<20}| Total Given | Num Gifts | Average Gift".format("Donor Name"))
    print("-" * 60)
    donor_list.sort(key=report_sort)
    for donor in donor_list:
        print("{:<21}${:>11.2f}{:>12}  ${:>12.2f}".format(donor[0], sum(donor[1]), len(donor[1]),
                                                          sum(donor[1]) / len(donor[1])))


# function for exit option off menu
def exit_program ():
    print("Program Exited!")
    sys.exit()


# main function run to start menu after donor list is loaded
def main():
    while True:
        response = input(prompt_menu)
        if response == "1":
            send_ty()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # Guards against code running automatically if module is imported
    main()
