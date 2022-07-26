import os
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader


def pdf_splitter(pdf_path, start_page, end_page, target_path=os.getcwd()):
    # we will save new splited pdf as "nameofpdf-splitted.pdf"
    # example if pdf name is "abc.pdf" then it will be saved as "abc-splitted(x-y).pdf"

    # Handling error if given file path is exit/correct or not.
    try:
        read_file = PdfFileReader(open(pdf_path, "rb"))  # read pdf
    except Exception as e:
        print("Oops!", type(e).__name__, "occurred.")
        print("Check your file path or file format.")
    else:
        no_of_pages = read_file.getNumPages()

        # Check input for start page and end page is correct.
        if not (start_page > 0 and end_page > 0 and start_page <= end_page and start_page <= no_of_pages and end_page <= no_of_pages):
            print("*" * 50)
            print("Invalid Agruments")
            print("*" * 50)
            print("Start and end page value must be positive.")
            print("*" * 50)
            print("Start_page must be less than equal to end page and total pages in the pdf.")
            print("*" * 50)
            print("End_page value must be less than no of pages in pdf.")
            print("*" * 50)
            print("Total no of pages in pdf is ", no_of_pages)

        else:
            pdf_filename = os.path.basename(pdf_path) # Get pdf file name from path
            new_file_name = pdf_filename.split(".")[0] + "-" + "splitted" + "(" + str(start_page) + "-" + str(end_page) + ")" + ".pdf"  # create file name for new pdf
            new_pdf = PdfFileWriter()  # create write object

            try:
                with open(os.path.join(target_path, new_file_name), "wb") as f:
                    for i in range(start_page - 1, end_page):
                        new_pdf.addPage(read_file.getPage(i))
                        new_pdf.write(f)
            except Exception as e:
                print("Oops!", type(e).__name__, "occurred.")
                print("Check your file path, target path or file format.")
            else:
                print("Task done successfully.")
                print("Splitted pdf", new_file_name,"saved to", target_path.split('/')[-1]+".")


def main():
    # First step is to check all command line arguments
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        # if arguments are less then 4 then we will show error message to users.
        print("*" * 50)
        print("Invalid Agruments")
        print("-" * 50)
        print("python pdf_split_all.py pdf_file_name_with_full_path starting_page, end_page, target_path(default is current directory)")
        print("-" * 50)
        print("Example")
        print("python pdf_split_all.py path 1 4 target_path(defaulf set to Documents)")
        print("*" * 50)
    elif len(sys.argv) == 4:
        # file name of PDF file which user want to split
        file_path = sys.argv[1] # pdf file path
        start_page = int(sys.argv[2])  # start page number
        end_page = int(sys.argv[3])  # end page number

        if not file_path.split(".")[-1] == "pdf":
            print("Only pdf file is accepted.")
        else:
            try:
                pdf_splitter(file_path, start_page, end_page)
            
            except Exception as e:
                print("Oops!", type(e).__name__, "occurred.")
                print("Check your file path, target path or file format.")
            

    elif len(sys.argv) == 5:
        # file name of PDF file which user want to split
        file_path = sys.argv[1]
        start_page = int(sys.argv[2])  # start page number
        end_page = int(sys.argv[3])  # end page number
        target_path = sys.argv[4]  # target path

        if not file_path.split(".")[-1] == "pdf":
            print("Only pdf file is accepted.")
        else:
            try:
                pdf_splitter(file_path, start_page, end_page, target_path)
            except Exception as e:
                print("Oops!", type(e).__name__, "occurred.")
                print("Check your file path, target path or file format.")


if __name__ == "__main__":
    # calling the main function
    main()
