import os
import cohere

api_key = "IhN5lW0oIRGN4RawcjIE3omb2IcwPtulPlGSNMHi"


#Koxej3ycFau3fv9shEy7X7mtjrY8jTImP2fi6NAt

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

  # Ensure at least one prompt is available
  if len(userPrompts) < 1:
    return 'At least one dance move prompt is required.'

  # Base prompt
  base_prompt = (
    f'Please pretend you are in the movie {movieTitle}. '
    f'The writers of the movie were not happy with the way the plot was written, here is what they changed about the movie: {userPrompts}.'
    'Describe to me 3 very specific scenes that happen in this new version of the movie occurring as a result of the change that the writers made.'
    'Do not mention the old version of the movie at all in your response. '
    'Do not talk about the film from an outside perspective, i.e you cannot use the film as a subject or an object because you do not know you are in a film.'
    'To reiterate, you cannot use the word film or any synonym of it and you cannot use the word scene or any synonym of it. '
    'Can you give me the 3 points in a matter-of-fact way as if they happened, not just in a movie?'
        # 'Your job is to be the author of the movie given in the prompt.'
    # 'You are the author of the movie and you will rewrite the alternative storyline based on the change to the story that the prompt gives.'
    # #'The story should be in the tone of a very good story teller. '
    # 'You will output a maximum of 3 main plot events to highlight the alterate timeline, but you will tell it from the perspective of a third person narrator, like a written storybook of the movie.'

  )



  # Generate lyrics
  response = co.generate(
    model='command-light',
    prompt=base_prompt,
    max_tokens=800,
    temperature=1.1,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE'
  )


  return response.generations[0].text

def formatStory(storyText):
    """
    Format the generated story to remove unnecessary comments and bullet points.

    :param storyText: The text of the generated story.
    :type storyText: str
    :return: The formatted story.
    """
    # Initialize the Cohere client
    co = cohere.Client(api_key)

    # Formatting prompt for Cohere
    formatting_prompt = (
        f"Here is a text generated by a story generator:\n\n{storyText}\n\n"
        "Please format this text by removing any unnecessary comments, bullet points, or non-story related content. "
        "Keep only the narrative parts of the story. Format it like a continuous narrative, ensuring it reads smoothly as a story."
    )

    # Generate formatted story
    formatted_response = co.generate(
        model='command-light',
        prompt=formatting_prompt,
        max_tokens=800,
        temperature=1.1,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE'
    )

    return formatted_response.generations[0].text
