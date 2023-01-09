import random
# Generate books
tickets = {}
books = []
def print_line(ln):
    string_line = ""
    for number in ln:
        if number == 0:
            string_line += "  |"
        elif number < 10:
            string_line += "0"+str(number)+"|"
        else:
            string_line += str(number)+"|"
    print(string_line)
    string_line += "\n"
def generate_books(n=1):
    for i in range(n):
        # numbers by column
        numbers = [[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19],[20,21,22,23,24,25,26,27,28,29],[30,31,32,33,34,35,36,37,38,39],[40,41,42,43,44,45,46,47,48,49],[50,51,52,53,54,55,56,57,58,59],[60,61,62,63,64,65,66,67,68,69],[70,71,72,73,74,75,76,77,78,79],[80,81,82,83,84,85,86,87,88,89,90]]
        book = {}
        book_raw = []
        # 18 rows in a book
        for r in range(18):
            # if the length of any column is equal to the rows remaining, then a number MUST be drawn from that column
            cols =[]
            for c in range(0,9):
                if numbers[c] != []:
                    cols.append(c)
            line = [0,0,0,0,0,0,0,0,0]
            forced_count = 0
            col_count = 0
            for column in numbers:
                if len(column) == 18-r:
                    forced_count += 1
                    number = random.choice(column)
                    line[col_count] = number
                    column.remove(number)
                    cols.remove(col_count)
                col_count += 1
            for n in range(5-forced_count):
                col = random.choice(cols)
                number = random.choice(numbers[col])
                line[col] = number
                cols.remove(col)
                numbers[col].remove(number)
            book_raw.append(line)
        # Assign lines to tickets
        book = {str(i+1)+"1":[book_raw[0],book_raw[1],book_raw[2]],str(i+1)+"2":[book_raw[3],book_raw[4],book_raw[5]],str(i+1)+"3":[book_raw[6],book_raw[7],book_raw[8]],str(i+1)+"4":[book_raw[9],book_raw[10],book_raw[11]],str(i+1)+"5":[book_raw[12],book_raw[13],book_raw[14]],str(i+1)+"6":[book_raw[15],book_raw[16],book_raw[17]]}
        books.append(book)
        tickets[str(i+1)+"1"] = [book_raw[0],book_raw[1],book_raw[2]]
        tickets[str(i+1)+"2"] = [book_raw[3],book_raw[4],book_raw[5]]
        tickets[str(i+1)+"3"] = [book_raw[6],book_raw[7],book_raw[8]]
        tickets[str(i+1)+"4"] = [book_raw[9],book_raw[10],book_raw[11]]
        tickets[str(i+1)+"5"] = [book_raw[12],book_raw[13],book_raw[14]]
        tickets[str(i+1)+"6"] = [book_raw[15],book_raw[16],book_raw[17]]
    # print books
    book_count = 0
    for book in books:
        book_count += 1
        print("Book no:",book_count)
        ticket_no = ""
        for ticket in book:
            if ticket_no != ticket:
                print("Ticket number:", ticket)
                ticket_no = ticket
            for line in book[ticket]:
                print_line(line)
        print("\n\n")

# Start game
stakes = ["invalid","Single line","Double line","FULL HOUSE"]
def start_game():
    # Generate numbers for game
    numbers = []
    for i in range(90):
        numbers.append(i+1)
    # Randomise game numbers
    game_numbers = []
    for i in range(90):
        ind = random.randint(0,len(numbers)-1)
        game_numbers.append(numbers[ind])
        numbers.pop(ind)
    stk = 1 # 1 indicates single line, 2 double line, 3 house
    called_numbers = []
    for number in game_numbers:
        response = input("\n[C], [Rtrn] to Check claim\n[B], [Rtrn] for numbers called so far\n[Rtrn] for next number\n:").upper()
        if stk < 4:
            if response == "C":
                ticket_no = input("Enter ticket no: ")
                try:
                    if check_claim(ticket_no, stk, called_numbers):
                        print("WINNER!")
                        print(stakes[stk])
                        stk += 1
                    else:
                        print("False claim")
                except:
                    print("Invalid ticket number")
            elif response == "B":
                called_numbers.sort()
                print("Numbers called so far:",called_numbers)
            else:
                print("Playing for",stakes[stk],"\n[",len(called_numbers)+1,"]",number)
                called_numbers.append(number)
        else:
            print("Game ending...")
            break

# Check claim
def check_claim(tn,stk,called):
    tk = tickets[tn]
    # print ticket being checked and count lines completed
    print("Checking ticket no",tn, "for",stakes[stk].lower())
    #string_line = ""
    lines_complete = 0
    for line in tk:
        print_line(line)
        # check numbers on line
        numbers_remaining = []
        numbers_remaining_clone = []
        for number in line:
            if number > 0:
                numbers_remaining.append(number)
                numbers_remaining_clone.append(number)
        for number in numbers_remaining_clone:
            if number in called:
                numbers_remaining.remove(number)
        if len(numbers_remaining) == 0:
            lines_complete += 1
        print("Numbers not called on line above:",numbers_remaining)
    if lines_complete >= stk:
        return True
    else:
        return False
invalid_choice = True
while invalid_choice:
    try:
        generate_books(int(input("How many books do you need? : ")))
        invalid_choice = False
    except:
        print("Error! Please enter an integer.")
        invalid_choice = True
start_game()
