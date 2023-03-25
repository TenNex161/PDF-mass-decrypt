import os
from pypdf import PdfReader, PdfWriter

#Get Infos from Input
def infos():
    global path
    global path_out
    path = str(input("Enter input path: "))
    path_out = str(input("Enter output path: "))

    #Complete paths to avoid errors
    if not path.endswith("/"):
        path = path + "/"
    if not path_out.endswith("/"):
        path_out = path_out + "/"

    #Filter for specific filenames
    filter_ = str(input("Enter filter (if none leave empty): "))
    try:
        #Get list of filenames
        files = [i for i in os.listdir(path) if i.lower().endswith(".pdf")]
        #Filter for filenames if a string was entered
        if filter_ != "":
            files = [i for i in files if (filter_) in i]
        #Raise exception if there are no files
        if len(files) == 0:
            raise Exception()
    except:
        #Error Message with former input
        print("** Input path not valid or no PDFs found")
        print("** Entered input path: " + str(path))
        print("** Entered filter: " + str(filter_))
        print("")
        #Call infos() again
        infos()
    else:
        #Print Message with number of files found and return file list
        print(str(len(files)) + " PDF(s) found")
        return files

#Get password(s) from input
def password():
    #Define password list
    pw = []

    #Function for repeated password input
    def p():
        x = input("Enter password: ")
        #Check if entered password is empty
        if len(x) == 0:
            p()
        #Add Password to list
        pw.append(str(x))
        #Ask for more passwords
        if input("Additional password? (y/n) ").lower() == "y":
            p()

    #Start p() and return list of passwords afterwards
    p()
    return pw


#Check and decrypt files
def decrypt(files, pw):
    #Count decrypted files
    count = 0

    #Iterate over filenames
    for i in files:
        #initialize reader with pdf file
        try:
            reader = PdfReader(path + "/" + i)
            writer = PdfWriter()
            #check if files are encrypted by only decrypting unreadable files
            if reader.is_encrypted:
                try:
                    len(reader.pages)
                except:
                    for j in pw:
                        try:
                            reader.decrypt(j)

                            # Add all pages to the writer
                            for page in reader.pages:
                                writer.add_page(page)

                            # Save the new PDF to a file
                            with open(path_out + i, "wb") as f:
                                writer.write(f)
                            count += 1


                        except:
                            pass
        except:
            print("**" + str(i) + ": File could not be read")

    print(str(count) + " PDF(s) decrypted")

files = infos()
pw = password()
decrypt(files, pw)
