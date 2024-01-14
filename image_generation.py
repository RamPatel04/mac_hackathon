import subprocess

def run_bing_image_creator(prompt, output_dir, max_retries=3):
    command = [
        "python",
        "-m",
        "BingImageCreator",
        "-U",
        "1nVIOdWy-BFTw_krLqJjgKR6oj-Yp4SfzOvM4WVFjdMsEGpJrF-KM98PmUqP7wHO8UQ_3R5vaKzd_h43eLHGjmiwxiSlI3uogsQCTLMGP7azFceq_j2AGj3RWFdv6DGpiztwanEOuKnNxyr1lpINpflbvgWpYLuVJx5jqgsR_KRbthp8JaTLF4_SF1TiSWqMSYRAi_Ro1zinl5GaI77Uxb8QjwCmw3KkgP0C0LGE6dHA",
        "--prompt",
        prompt,
        "--output-dir",
        output_dir,
    ]

    attempt = 0
    while attempt < max_retries:
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Command executed successfully for prompt: {prompt}")
            return
        except subprocess.CalledProcessError as e:
            attempt += 1
            print(f"Attempt {attempt} failed. Error:\n{e.stderr.decode()}")
            if "Redirect failed" in e.stderr.decode():
                print("Redirect failed. Retrying...")
                continue
            else:
                return
    print(f"Command failed after {max_retries} attempts for prompt: {prompt}")