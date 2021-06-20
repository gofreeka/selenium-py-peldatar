columns = " "
stp_one = 9
stp_two = 18

for i in range(97, 122):
    if i < 105:
        columns = ((chr(i) + " " + str(i) + "\t") +
                   (chr(i + stp_one) + " " + str(i + stp_one) + "\t") +
                   (chr(i + stp_two) + " " + str(i + stp_two) + "\t"))
        print(columns)
