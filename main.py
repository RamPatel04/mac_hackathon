import os
import asyncio
from story_generation import alternateStoryGen
from image_generation import generate_image_with_prompt

# create python function
def main():
    # get user input
    user_input = input("Enter your prompt: ")

    # call image generation function
    this_directory = os.getcwd()
    asyncio.run(generate_image_with_prompt(user_input, this_directory))
    # print outputG
    # print(output)


# call main function
if __name__ == '__main__':
    main()