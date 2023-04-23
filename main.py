import requests, hashlib, datetime, random, os, pyfiglet, time
from brute import brute


def request_api_data(query_char):
    # check the API
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error Fetching: {res.status_code},Check The API And Try Again")
    return res


def internet_on():
    # check internet connection
    try:
        res = requests.get("http://www.google.com")
    except :
        return False
    else:
        return True


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check password if exists in api response
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(password):
    # Check for one password
    count = pwned_api_check(password)
    if count:
        print("")
        print(f"\033[1;31;1m{password}\033[m",end="  ")
        print(f"Was Found {count} Times!")
    else:
        print("")
        print(f"\033[1;31;1m{password}\033[m", end="  ")
        print("Was Not Found! Good Job\n")
    return "Done!"


def valid_date(year, month, day):
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return False


def generator():
    f_name = str(input("\n[+] Enter Your Name: "))
    if f_name != "":
        while not f_name.isalpha():
            print("[*] Your Name Must Have Only Letters")
            f_name = str(input("\n[+] Enter Your Name: "))
    l_name = input("\n[+] Enter Your Lastname: ")
    if l_name != "":
        while not l_name.isalpha():
            print("[*] Your Lastname Must Have Only Letters")
            l_name = str(input("\n[+] Enter Your Lastname: "))
    b_date = input("\n[+] Enter Your Birthdate (DD/MM/YEAR): ")
    if b_date != "":
        while b_date.isalpha():
            print("[*] Birthday Must Be Numbers")
            b_date = input("\n[+] Enter Your Birthdate (DD/MM/YEAR): ")
        day = b_date[:2]
        month = b_date[3:5]
        year = b_date[6:]
        while valid_date(year, month, day) == False:
            print("[*] Invalid Birthdate")
            b_date = input("\n[+] Enter Your Birthdate (DD/MM/YEAR): ")
            day = b_date[:2]
            month = b_date[3:5]
            year = b_date[6:]
    elif b_date == "":
        day, new, month, year = "", "", "", ""
    other_w = input("\n[+] Any Other Information To Add To The Password?: ")
    new = [f_name.capitalize(), l_name.capitalize(), other_w]
    random.shuffle(new)
    new = new[0] + new[1] + new[2]
    pass_list = [day, new, month, year]
    random.shuffle(pass_list)
    password = ""
    password = password.join(pass_list)
    if password == "":
        print("\n[*] You Didn't Enter Anything,Password Is Empty")
    print("\n")
    if password != "":
        print(f"[*] The Password Is : " + f"\033[1;32;1m {password}\033[m")
        if internet_on():
            (main(password))
        else:
            print("\033[1:32:1m\n[*] No Internet Connection To Check The Password...\033[m")
    print("\n[**] Thank You For Using !")
    return password

k = True
while k:
    while True:
        try:
            os.system("clear")
            pyfiglet.print_figlet("Password Master ", "standard", "RED")
            choice = int(input(
                "\n[1] Check Password Strength  \n\n[2] Generate Passwords \n\n[0] To Exit \n\n[+] What To Do? "))
        except ValueError:
            os.system("clear")
            pyfiglet.print_figlet("Password Master ", "standard", "RED")
            print(f"\033[1;31;1m \n[*] Wrong Input,Only Numbers Please \033[m")
            time.sleep(1)
        else:
            break
    if choice > 2:
        os.system("clear")
        pyfiglet.print_figlet("Password Master ", "standard", "RED")
        print("\033[1;31;1m\n[*] No Such Number, What To Do? \033[m")
        time.sleep(1)
    if choice == 1:
        if internet_on():
            while True:
                while True:
                    try:
                        os.system("clear")
                        pyfiglet.print_figlet("Password Master ", "standard", "RED")
                        print("[1] Check One Password \n\n[2] Check File That Contain Passwords \n\n[0] Go Back \n")
                        chc_text = int(input("[+] What To Do? "))
                    except ValueError:
                        os.system("clear")
                        pyfiglet.print_figlet("Password Master", "standard", "RED")
                        print("\033[1;31;1m\n[*] Wrong Input,Only Numbers Please\033[m")
                        time.sleep(1)
                    else:
                        break
                if chc_text < 3 and chc_text >= 0:
                    if chc_text == 1:
                        password = input("\n[+] Your Password: ")
                        (main(password))
                        answer = input("\n[*] Do You Want To Try Another Password?(Y/N) ")
                        if answer == "N" or answer == "n":
                            print("\n[**] Thanks For Using ")
                            k = 0
                            break
                    if chc_text == 2:
                        while True:
                            text_path = input("\n[+] Enter File Path Please: ")
                            if os.path.exists(text_path):
                                with open(text_path) as fp:
                                    line = fp.readline().strip()
                                    while line:
                                        main(line)
                                        line = fp.readline().strip()
                                break
                            else:
                                print("\n[*] File Not Found")
                        input("\n[*] Press Any Key To Continue...")
                    break
                else:
                    os.system("clear")
                    pyfiglet.print_figlet("Password Maste r", "standard", "RED")
                    print("\033[1;31;1m\n[*] No Such Number\033[m")
                    time.sleep(1)
        if not internet_on():
            os.system("clear")
            input("\033[1;32;1m\n[**] No Internet Connection,Check You Internet And Try Again\033[m")
    elif choice == 2:
        os.system("clear")
        pyfiglet.print_figlet("Password Master ", "standard", "RED")
        generate_num = 0
        while generate_num < 1:
            try:
                generate_num = int(input("[+] How Many Password You Want To Generate? "))
            except ValueError:
                print("\033[1;31;1m\n[*] Enter Number Please\033[m\n")
        if generate_num == 1:
            generator()
            k = 0
        elif generate_num > 1:
            file_name = datetime.datetime.now()
            file_name = file_name.replace(microsecond=0)
            output_path = input("\n[+] Path To Save The File or Enter To Save It In This Directory:")
            if output_path == "":
                output_path = os.getcwd()
            while not os.path.exists(output_path):
                print("\033[1;31;1m\n[*] Path Does Not Exists!\033[m")
                output_path = input("\n[+] Path To Save The File or Enter To Save It In This Directory:")
                if output_path == "":
                    output_path = os.getcwd()
            while generate_num > 0:
                print(generator(), file=open(f"{output_path}/{file_name}.txt", "a"))
                generate_num -= 1
                os.system("clear")
                pyfiglet.print_figlet("Password Master ", "standard", "RED")
                print(f"\n[*] Still {generate_num} Password To Do")
            k = 0
    elif choice == 0:
        k = 0
        print("\n[**] Thank You For Using ")
        os.system("clear")
        break
