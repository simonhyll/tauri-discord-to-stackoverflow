import os
import openai
from dotenv import load_dotenv

load_dotenv()  

openai.api_key = os.getenv('OPENAI_API_KEY')


# predefined stackoverflow structure
so_post_structure = {
    'title': '# {title}\n',
    'question': '## Question\n\n### {question}\n\n{details}\n\n**Tags:** {tags}\n',
    'answer': '## Answer\n\n{answer}\n'
}

def create_so_post(path):
    with open(path, 'r') as file:
        content = file.read()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[{
            "role":"user",
            "content":"""Use the following markdown format for your response:

# Title in the form of a question
## Question
Question body
## Answer
Answer body
            
Translate the following input taken from the Tauri discord server into a question and answer appropriate for StackOverflow, cleaning it up and improving it as appropriate:

""" + content
        }]
    )

    return response.choices[0].message.content.strip()

def convert_files_to_so(input_directory_path, output_directory_path):
    if not os.path.exists(output_directory_path):
        os.makedirs(output_directory_path)
    for filename in os.listdir(input_directory_path):
        if os.path.exists(os.path.join(output_directory_path, filename)):
            print("Skipping: " + os.path.join(output_directory_path, filename))
            continue
        if filename.endswith(".md"):
            print("Generating: " + os.path.join(output_directory_path, filename))
            so_post = create_so_post(os.path.join(input_directory_path, filename))

            with open(os.path.join(output_directory_path, filename), 'w') as output_file:
                output_file.write(so_post)

def generate_summary(output_directory_path):
    summary_lines = ["# Summary\n", "[Introduction](./introduction.md)\n", "- [#support](./support.md)\n"]

    for filename in sorted(os.listdir(output_directory_path)):
        if filename.endswith(".md"):
            line = f"  - [{filename.replace('.md', '')}](./support/{filename})\n"
            summary_lines.append(line)

    with open('src/SUMMARY.md', 'w') as summary_file:
        summary_file.writelines(summary_lines)

def main():
    input_folder = 'input/support'
    output_folder = 'src/support'
    convert_files_to_so(input_folder, output_folder)
    generate_summary(output_folder)

if __name__ == "__main__":
    main()
