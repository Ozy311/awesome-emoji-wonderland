#!/usr/bin/env python3
"""
🧜‍♀️ Magical Mermaid Riding a Unicorn 🦄
A whimsical ASCII art animation script
"""
import os
import time
import random
import sys

# ANSI color codes for rainbow effect
COLORS = [
    '\033[91m',  # Red
    '\033[93m',  # Yellow
    '\033[92m',  # Green
    '\033[96m',  # Cyan
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[0m',   # Reset
]

# ASCII Art of Mermaid riding a Unicorn
MERMAID_UNICORN = [
    r"                                  ",
    r"       *                          ",
    r"                      *           ",
    r"                                  ",
    r"       .                   *      ",
    r"            *                     ",
    r"                                  ",
    r"     *             ___            ",
    r"               ,~'_____`.       * ",
    r"  *           / / ,-. \ \         ",
    r"             ( ( ( o ) ) )        ",
    r"              \ \ `-' / /      .  ",
    r"        .      `._____,'          ",
    r"                   |              ",
    r"        *         / \        *    ",
    r"                 /   \            ",
    r"              --'     `--         ",
    r"      *             *             ",
    r"         /)                       ",
    r"        //\     __ _              ",
    r"    .  / | \   /\*/--             ",
    r"       *|/\|*  \/x\_ *            ",
    r"        |  |    |/ \         *    ",
    r"      * |\/|*   |\  \            ",
    r"         V V    V V             . ",
    r"     ~~~~~~~~~~~~~~~~~~~~~~~~~     ",
    r"  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ",
    r" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
    r"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ",
]

# Decorative stars to sprinkle in the background
STARS = ['✦', '✧', '*', '✪', '⋆', '✫', '✴']

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def apply_rainbow_colors(art):
    """Apply rainbow colors to the ASCII art."""
    colored_art = []
    for line in art:
        colored_line = ""
        for char in line:
            if char not in " ":
                colored_line += random.choice(COLORS) + char + '\033[0m'
            else:
                colored_line += char
        colored_art.append(colored_line)
    return colored_art

def add_stars(art, width):
    """Add random stars to the ASCII art."""
    art_with_stars = art.copy()
    for i in range(len(art)):
        line = list(art[i])
        for j in range(len(line)):
            if line[j] == ' ' and random.random() < 0.01:  # 1% chance of star
                line[j] = random.choice(STARS)
        art_with_stars[i] = ''.join(line)
    return art_with_stars

def scroll_art(art, screen_width=80, screen_height=30, speed=0.1):
    """Scroll the ASCII art across the screen."""
    colored_art = apply_rainbow_colors(art)
    
    for start_col in range(screen_width, -len(max(art, key=len)), -1):
        clear_screen()
        
        # Add stars to create magical effect
        starry_art = add_stars(colored_art, screen_width)
        
        for i, line in enumerate(starry_art):
            if i < screen_height:
                # Calculate padding
                if start_col > 0:
                    padding = ' ' * start_col
                    print(padding + line)
                else:
                    # If start_col is negative, we need to slice the line
                    visible_part = line[abs(start_col):]
                    print(visible_part)
        
        # Print a magical tagline at the bottom
        print("\n" + random.choice(COLORS) + "✨ Where dreams and magic collide! ✨" + '\033[0m')
        
        # Sleep to control animation speed
        time.sleep(speed)

def main():
    """Run the mermaid riding unicorn animation."""
    try:
        # Get terminal size
        term_width = os.get_terminal_size().columns
        term_height = os.get_terminal_size().lines
    except:
        # Fallback if terminal size cannot be determined
        term_width = 80
        term_height = 30
    
    # Infinite loop for continuous animation
    try:
        cycles = 0
        while True:
            scroll_art(MERMAID_UNICORN, term_width, term_height)
            cycles += 1
            # Every 3 cycles, reverse the animation for fun
            if cycles % 3 == 0:
                # Scroll backwards
                reversed_art = MERMAID_UNICORN.copy()
                for i in range(len(reversed_art)):
                    reversed_art[i] = reversed_art[i][::-1]
                
                for start_col in range(-len(max(reversed_art, key=len)), term_width):
                    clear_screen()
                    starry_art = add_stars(apply_rainbow_colors(reversed_art), term_width)
                    
                    for i, line in enumerate(starry_art):
                        if i < term_height:
                            if start_col > 0:
                                padding = ' ' * start_col
                                print(padding + line)
                            else:
                                visible_part = line[abs(start_col):]
                                print(visible_part)
                    
                    print("\n" + random.choice(COLORS) + "✨ Magic is happening in reverse! ✨" + '\033[0m')
                    time.sleep(speed)
    
    except KeyboardInterrupt:
        clear_screen()
        print(random.choice(COLORS) + "Thanks for watching the magical mermaid and unicorn show!" + '\033[0m')
        sys.exit(0)

if __name__ == "__main__":
    print("Press Ctrl+C to exit the magical journey...")
    time.sleep(2)
    main()