<div align="center">

# Discord to StackOverflow<br/>Post generator

</div>

## Getting started

You'll need to create the `input/support/` folder manually for now. To learn more about how to do it, start the mdbook and read about it there.

You'll also need to set up a `.env` file with your OpenAI API key.

```bash
# Install mdbook
cargo install mdbook
# Install dependencies
python3 -m pip install openai python-dotenv
# Generate the posts
python3 generate.py
# I tend to serve mdbook on some random port
mdbook serve --port 8686
```

## Privacy

While the generated mdbook has any and all personal information removed from it the raw input might not be as privacy friendly. For this reason I've added the input folder to .gitignore. In reality of course there shouldn't be any private information in the input folder because it's just ctrl + c, ctrl + v from the Discord server where this information is residing perfectly publicly, so if there is any sensitive information in it it's already being exposed there.

I might decide to commit the input as well, but I want to talk it through with someone else first, make sure I'm not violating someones privacy. I mean, it's all already publicly available in the server, so I don't see how putting it on Github could hurt, but still, privacy is a serious matter.

Since the data sent to ChatGPT is already publicly available data, there shouldn't be any issues with sharing data with it.
