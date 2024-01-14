from BingImageCreator_modified.src.BingImageCreator import ImageGenAsync
import asyncio

async def generate_image_with_prompt(prompt, output_dir, auth_cookie="1nVIOdWy-BFTw_krLqJjgKR6oj-Yp4SfzOvM4WVFjdMsEGpJrF-KM98PmUqP7wHO8UQ_3R5vaKzd_h43eLHGjmiwxiSlI3uogsQCTLMGP7azFceq_j2AGj3RWFdv6DGpiztwanEOuKnNxyr1lpINpflbvgWpYLuVJx5jqgsR_KRbthp8JaTLF4_SF1TiSWqMSYRAi_Ro1zinl5GaI77Uxb8QjwCmw3KkgP0C0LGE6dHA", debug_file=None, quiet=False, all_cookies=None):
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
    max_attempts = 5
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
