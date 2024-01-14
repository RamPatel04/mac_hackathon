import os
import cohere

api_key = "Koxej3ycFau3fv9shEy7X7mtjrY8jTImP2fi6NAt"

def alternateStoryGen(movieTitle, userPrompts):
  """
  Generate an alternate story based on the given prompts.

    :param prompts: A list of prompts to use for the story generation.
    :type prompts: list
    :return: The generated story.
    
  IDEAS:  
    - Generate multiple timelines (Parallel Timeline Generator)
  """

  # Initialize the Cohere client
  co = cohere.Client(api_key)

  # Base prompt
  base_prompt = (
    # #'Your job is to generate an alternate story timeline based on the given prompts. '
    # 'Your job is to be the author of the movie given in the prompt.'
    # 'You are the author of the movie and you will rewrite the alternative storyline based on the change to the story that the prompt gives.'
    # #'The story should be in the tone of a very good story teller. '
    # 'You will output a maximum of 3 main plot events to highlight the alterate timeline, but you will tell it from the perspective of a third person narrator, like a written storybook of the movie.'

  )

  # Ensure at least one prompt is available
  if len(userPrompts) < 1:
    return 'At least one dance move prompt is required.'

  # Add the mandatory first dance move prompt for the verse
  formatted_prompt = f"{base_prompt} Here are the user's prompts:\n\n{userPrompts}\n\n"


  # Generate lyrics
  response = co.generate(
    model='command',
    prompt=formatted_prompt,
    max_tokens=128,
    temperature=1.5,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE'
  )

  # TODO: save lyrics ot a text file

  return response.generations[0].text