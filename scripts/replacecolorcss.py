import re

# Define a function to check if a color is a shade of green or teal
def is_shade_of_green_or_teal(color):
    # Regex patterns to match color formats
    hex_pattern = re.compile(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
    rgb_pattern = re.compile(r'^rgb\((\d{1,3}), (\d{1,3}), (\d{1,3})\)$')
    named_colors = ['green', 'lime', 'teal', 'olive', 'aqua', 'aquamarine', 'chartreuse', 'forestgreen', 'greenyellow', 'lightgreen', 'mediumseagreen', 'mediumspringgreen', 'palegreen', 'seagreen', 'springgreen', 'yellowgreen']

    # Check for hex colors
    if hex_pattern.match(color):
        hex_value = color.lstrip('#')
        if len(hex_value) == 3:
            hex_value = ''.join([c*2 for c in hex_value])
        r, g, b = int(hex_value[:2], 16), int(hex_value[2:4], 16), int(hex_value[4:6], 16)
    # Check for RGB colors
    elif rgb_pattern.match(color):
        r, g, b = map(int, rgb_pattern.match(color).groups())
    # Check for named colors
    elif color in named_colors:
        return True
    else:
        return False

    # Define thresholds for green and teal shades
    return (g > 100 and r < 150 and b < 150) or (g > 100 and b > 100)

# Function to replace shades of green or teal with black in a CSS file
def replace_green_with_black(file_path):
    with open(file_path, 'r') as file:
        css_content = file.read()

    # Replace green/teal shades with black
    def replace_color(match):
        color = match.group(0)
        if is_shade_of_green_or_teal(color):
            return 'black'
        return color

    updated_css_content = re.sub(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})|rgb\(\d{1,3}, \d{1,3}, \d{1,3}\)|\b[a-zA-Z]+\b', replace_color, css_content)

    # Save the updated CSS content to a new file
    with open('updated_' + file_path, 'w') as file:
        file.write(updated_css_content)

# Usage example
replace_green_with_black('awf.css')
