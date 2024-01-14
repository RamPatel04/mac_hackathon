import os
# import re
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
    formatted_output = formatStory(output)

    # bullet_points = re.findall(r'\d+\.\s+"([^"]+)"', output)
    # bullet_points_str = ' '.join(bullet_points)

    asyncio.run(generate_image_with_prompt(formatted_output, this_directory))
    # print outputG
    print(formatted_output)


# call main function
if __name__ == '__main__':
    main()