from fuzzing.fuzzer import FuzzExecutor

# Files to use as initial input seed.
file_list = ["./examples/test_string.txt"]
#["./pdf/2017-12-02_Dagbladet_Information_-_02-12_2017.pdf",
# "./pdf/CV_eng_2015.pdf", "./pdf/PID3286025.pdf"]

# List of applications to test.
apps_under_test = ["python rle.py -e".replace(" ","&")
                #"/Applications/Adobe Acrobat DC/Adobe Acrobat.app/Contents/MacOS/AdobeAcrobat",
                   #"/Applications/PDFpen 6.app/Contents/MacOS/PDFpen 6",
                   #"/Applications/Preview.app/Contents/MacOS/Preview",
                   ]

number_of_runs = 13

def test():
    print("start test")
    fuzz_executor = FuzzExecutor(apps_under_test, file_list)
    fuzz_executor.run_test(number_of_runs)
    print("Tests finished")
    return fuzz_executor.stats

def main():
    print("Hello")
    stats = test()
    print(stats)

if __name__ == "__main__":
    main()
