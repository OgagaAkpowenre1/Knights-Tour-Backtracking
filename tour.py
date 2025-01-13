import streamlit as st
import time
from PIL import Image, ImageDraw
import random

def draw_chessboard():
    board = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(board)
    
    square_size = 50
    
    for row in range(8):
        for col in range(8):
            color = "black" if (row + col) % 2 == 0 else "white"
            draw.rectangle([col * square_size, row * square_size, (col + 1) * square_size, (row + 1) * square_size], fill=color)
            
    return board

def draw_knight(board, position):
    knight_image = Image.new("RGBA", (50, 50), (255, 0, 0, 255))
    knight_draw = ImageDraw.Draw(knight_image)
    knight_draw.ellipse([10, 10, 40, 40], fill="gray")
    
    board.paste(knight_image, (position[1] * 50, position[0] * 50), knight_image)

def knight_moves(position):
    # Define all possible knight moves
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    possible_moves = [(position[0] + move[0], position[1] + move[1]) for move in moves]
    
    valid_moves = [move for move in possible_moves if 0 <= move[0] < 8 and 0 <= move[1] < 8]
    return valid_moves

st.set_page_config(page_title="Knight's Tour", layout="centered")
st.title("Knight's Tour Visualizer")
st.header("Welcome to the Knight's Tour App")
st.subheader("The Knight's Tour is a mathematical problem involving a knight on a chessboard. The knight is placed on the first square of an empty board and, moving according to the rules of chess, must visit each square exactly once.")

st.write("The knight has the unique ability to move in an L-shape: two squares in one direction and then one square perpendicular to that. The knight can move to any of the squares on the chessboard, but it cannot visit the same square twice.")

st.markdown("""
            - Choose the type of tour you wish to see\n
            - Adjust the speed of the knight's movement\n
            - Pause the animation at any point\n
            """)

# Initialize knight position in session state
if "knight_position" not in st.session_state:
    st.session_state.knight_position = (0, 0)

# Initialize paused state in session state
if "paused" not in st.session_state:
    st.session_state.paused = False

# Button to toggle pause/play
if st.button("Pause/Play"):
    st.session_state.paused = not st.session_state.paused

# If the animation is not paused, move the knight

    if not st.session_state.paused:
        possible_positions = knight_moves(st.session_state.knight_position)
        if possible_positions:
            st.session_state.knight_position = random.choice(possible_positions)

    # time.sleep(0.5)  # Delay to make the animation visible

# Draw the chessboard with the knight
board_with_knight = draw_chessboard()
draw_knight(board_with_knight, st.session_state.knight_position)

# Display the chessboard image
st.image(board_with_knight, caption="Knight's Position", use_column_width=True)

# Display the pause/play status
st.write(f"Animation {'Paused' if st.session_state.paused else 'Running'}")

