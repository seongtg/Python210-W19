#   ------------------------------------#
#   Title: Mailroom Part 1
#   Dev: SChang
#   Date: Feb 2nd, 2019
#   ChangeLog: (Who, When, What)
#   SChang,02/02/2019, Created Script
#   ------------------------------------#
import os
import sys
import math

donor_list = {"William Gates": [1010, 2020, 3030],
              "Mark Zuckerberg": [5500, 4400],
              "Jeff Bezos": [6745, 2345, 3845],
              "Paul Allen": [9999, 8888, 7777]
              }


#   function for sending either adding new donor or checking against donor list
def send_ty():
    DonorName = "list"
    while DonorName == "list":
        DonorName = input(""""Provide Donor Full Name, or type: "List" to display a list of all donors => """)
        if DonorName.lower().strip() == "list":
            view_donors()
            continue
        if DonorName[:1].lower() == "e":
            return None

    DonorName = DonorName.strip()
    donor_amount = ask_donation_amount(DonorName)
    if donor_amount is None:
        return None
    append_donation(DonorName, donor_amount)

    print(ty_letter(DonorName, donor_amount), end='\n\n')


#   function that recognizes name and donation amount which is passed through the send_ty function for print
def ty_letter(name,amount):
    return f"""
    Thank you, {name} for donating ${amount:.2f}"""


#   function that is passed through send_ty function defined by donor_amount
def ask_donation_amount(name):
    response = input(f"How much did {name} donate? ")
    if response [:1].lower() == 'e':
        return None
    return float(response)


#   function appending name/amount to the donor list if new
def append_donation(name, amount):
    donor_list.setdefault(name, []).append(amount)


# viewing list of donors if "List" is entered from menu
def view_donors():
    for donor in donor_list:
        print(f"{donor}")


def report_sort(item):
    return item[1]


# function for report that is formatted with donor information
def create_report():
    print()
    print("{:<20}| Total Given | Num Gifts | Average Gift".format("Donor Name"))
    print("-" * 60)

    for d, v in sorted(donor_list.items(), key=report_sort, reverse=True):
        print("{:<21}${:>11.2f}{:>12}  ${:>12.2f}".format(d, sum(v), len(v),

                                                          sum(v) / len(v)))


# function for exit option off menu
def exit_program ():
    print("Program Exited!")
    sys.exit()


def main():
    menu_dict = {
        "1": send_ty,
        "2": create_report,
        "3": exit_program
    }

    prompt_menu = "\n".join(("",
                             "Charity Management Application",
                             "Please choose from below options:",
                             "",
                             "1 - Send a Thank You",
                             "2 - Create a Report",
                             "3 - Exit",
                             ">>> "))

    while True:
        response = input(prompt_menu)
        menu_dict[response]()


if __name__ == "__main__":
    # Guards against code running automatically if module is imported
    main()
