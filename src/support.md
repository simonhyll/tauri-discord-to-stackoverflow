# #support

## Procedure:

1. Copy a posts thread ID
2. Create a new `input/support/threadID.md` file
3. Copy the contents of the post from Discord into the file, just marking all the contents and ctrl + c, ctrl + v
4. Run `python3 generate.py`

You can search all posts based on both their thread ID now and their title in Discord. Note that thread id's are the most accurate by far, title contents can get matches for a lot more posts than you want.

## Regenerate posts

To regenerate a post, in case you think ChatGPT can do better with another attempt, simply delete the post in `src/support/` and quickly re-run `python3 generate.py` before mdbook decides to generate an empty version of the file. Of course, you can also simply close mdbook so there's no time pressure while regenerating posts.
