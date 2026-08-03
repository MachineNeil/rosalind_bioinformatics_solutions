'''
Problem

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
Sample Dataset

Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat

Sample Output

Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat
'''

FILEPATH_READ = r"INI5_working_with_files\data.txt"
FILEPATH_WRITE = r"INI5_working_with_files\data_out.txt"

def main():
    with open(FILEPATH_READ) as f_read, open(FILEPATH_WRITE, "w") as f_write:
        for i, line in enumerate(f_read, start=1):
            if i % 2 != 0:
                f_write.write(line)

if __name__ == "__main__":
    main()