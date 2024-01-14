import os
import re
import asyncio
from story_generation import alternateStoryGen, formatStory
from image_generation import generate_image_with_prompt

# create python function
def main():
    # get user input
    movie = input("Enter the movie you would like to rewrite!: ")
    user_input = input("Enter your prompt: ")
    this_directory = os.getcwd()

    # call story generation function
    output = alternateStoryGen(movie, user_input)

    # format output for readability for users on the UI
    formatted_output = formatStory(output)

    # format output for the image generation
    pattern = r'\d\..*?(?=\n\d\.|\n\n|$)'
    matches = re.findall(pattern, output, re.DOTALL)
    combined_string = '\n'.join(matches)

    # call image generation function
    asyncio.run(generate_image_with_prompt(combined_string, this_directory))
    # print outputG
    print(formatted_output)

# call main function
if __name__ == '__main__':
    main()