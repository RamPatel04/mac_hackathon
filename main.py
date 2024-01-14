import os
from story_generation import alternateStoryGen
from image_generation import run_bing_image_creator

# create python function
def main():
    # get user input
    user_input = input("Enter your prompt: ")

    # call image generation function
    this_directory = os.getcwd()
    run_bing_image_creator(user_input, this_directory)
    # print outputG
    # print(output)


# call main function
if __name__ == '__main__':
    main()