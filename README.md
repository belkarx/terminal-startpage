# Terminal-y Startpage
## Setup
1. Clone the repository, then make an `unformatted.txt` file following the specifications in `example.txt`.

2. Run `format.py`

3. Open `index.hml` in your browser to ensure that the page looks as you intended

4. Set the page as your startpage. This process differs by browser. In firefox, go to Settings -> Home -> New Windows and Tabs -> Homepage and new windows, and set the "Custom Urls" option (above the Homepage and new windows text box). Then enter the path to `index.html` in the text box (ie `file:///home/user/projects/startpage/index.html`). I believe an extension or javascript-hacky skills are necessary for adding a startpage in Chrome.

## Modifications
The background image (`assets/background.jpg`) can be changed

The favicon image (`assets/favicon.jpg`) can be changed [I'd recommend making an icon and then resizing it to 8x8 or 16x16 in GIMP or whatever editor you wish]

Link color can be altered by changing `a:hover` in `main.css`

If a group of links is too long, you can manually mess with `index.html` to change it (but it should realistically be fine)


## Other notes
Weather data with icons is a WIP, I might not end up merging it because I like the simplicity of the look right now

Also this is intended for a few long lists of links, and the font size is hardcoded. This whole project was intended to be a quick utility for me so it's not very clean, but I figured someone might like the look and want to use it.

