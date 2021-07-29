import os

# Function to rename multiple files
def main():

    count = 1
    pwd = '/home/subhodeep/Documents/IIIT_Bangalore/Sem_2_2021/PE/CNN/Train/clockwise/'
    for count, filename in enumerate(os.listdir(pwd)):
        dst ="clockwise" + str(count) + ".png"
        src = pwd + filename
        dst = pwd + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
