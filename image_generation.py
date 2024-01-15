from BingImageCreator_modified.src.BingImageCreator import ImageGenAsync

async def generate_image_with_prompt(prompt, output_dir, auth_cookie="1wxTlQu1wLV04PTjmwQ6tDf-5FHdpWjsiPnGA72SNk6-9_iXfLXnSP6zFqUcNHKBdxa5D8BO3-G-hsTLt3JCqgyfPMoV_IeHLbbEfwOvmbiIBtQEZkg0sZPjYe5OHM2AXKpV_hTAkcLacOzR-ThuUrn8shu2Bw8Vnd879nwQSlYfBmxXHQZ-BHWPuwbKnBQ11n0nGso3tuoQVblrQgAl4NfOovachlh4mL24Ff4Yyo34", debug_file=None, quiet=False, all_cookies=None):
    """
    Generate an image using Bing Image Creator with a given prompt.

    Args:
    prompt (str): The prompt to generate an image for.
    output_dir (str): The directory to save the generated image.
    auth_cookie (str): Authentication cookie for Bing Image Creator.
    debug_file (str, optional): Path to a debug file. Defaults to None.
    quiet (bool, optional): Flag to disable pipeline messages. Defaults to False.
    all_cookies (list[dict], optional): Additional cookies if required. Defaults to None.

    Returns:
    None: The image is saved in the specified output directory.
    """
    max_attempts = 3
    attempt = 0
    while attempt < max_attempts:
        try:
            async with ImageGenAsync(auth_cookie, debug_file=debug_file, quiet=quiet, all_cookies=all_cookies) as image_generator:
                images = await image_generator.get_images(prompt)
                await image_generator.save_images(images, output_dir=output_dir, download_count=3)
            print("Image generation completed successfully.")
            break
        except Exception as e:
            if "Redirect failed" in str(e):
                attempt += 1
                print(f"Redirect failed, retrying... (Attempt {attempt}/{max_attempts})")
                if attempt == max_attempts:
                    print("Maximum retry attempts reached. Image generation failed.")
            else:
                print(f"An error occurred during image generation: {e}")
                break
