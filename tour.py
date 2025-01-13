import streamlit as st
import time
from PIL import Image, ImageDraw

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
    
knight_position = (0, 0)

def knight_moves(position):
    # Here we can define all possible knight moves
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    possible_moves = [(position[0] + move[0], position[1] + move[1]) for move in moves]
    return possible_moves


st.set_page_config(page_title="Knight's Tour", layout="centered")

st.title("Knight's Tour Visualizer")

st.header("Welcome to the Knight's Tour App")

st.subheader("The Knight's Tour is a mathematical problem involving a knight on a chessboard. The knight is placed on the first square of an empty board and, moving according to the rules of chess, must visit each square exactly once.")

st.write("The knight has the unique ability to move in an L-shape: two squares in one direction and then one square perpendicular to that. The knight can move to any of the squares on the chessboard, but it cannot visit the same square twice.")

st.markdown("""
            -Choose the type of tour you wish to see\n
            -Adjust the speed of the knight's movement\n
            -Pause the animation at any point\n
            """)

paused = st.button("Pause Animation")


board_with_knight = draw_chessboard()
draw_knight(board_with_knight, knight_position)
st.image(board_with_knight, caption="Knight's Position")


if paused:
    st.write("Animation paused")
else:
    st.write("Animation running")