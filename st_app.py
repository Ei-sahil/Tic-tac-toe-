import streamlit as st
import random

st.set_page_config(
    page_title="Tic-Tac-Toe",
    page_icon="⭕",
    layout="centered"
)

st.title("⭕ Tic-Tac-Toe")
st.write("Let's play!")


def check_winner():

    board = st.session_state.board

    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return board[row][0]

    # Check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != "":
            return board[0][column]

    # Check main diagonal
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    # Check other diagonal
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    # Check tie
    for row in range(3):
        for column in range(3):
            if board[row][column] == "":
                return None

    return "Tie"


def computer_move():
    board=st.session_state.board

    empty_cells=[]

    for row in range(3):
        for column in range(3):
            if board[row][column]=="":
                empty_cells.append((row,column))

    for row, column in empty_cells:

        board[row][column] = "o"

        if check_winner() == "o":
            board[row][column] = ""
            return row, column

        board[row][column] = ""

    for row, column in empty_cells:

        board[row][column] = "x"

        if check_winner() == "x":
            board[row][column] = ""
            return row, column

        board[row][column] = ""

    if board[1][1] == "":
        return 1, 1

    corners = [
        (0, 0),
        (0, 2),
        (2, 0),
        (2, 2)
    ]

    empty_corners = []

    for row, column in corners:
        if board[row][column] == "":
            empty_corners.append((row, column))

    if empty_corners:
        return random.choice(empty_corners)

    edges = [
        (0, 1),
        (1, 0),
        (1, 2),
        (2, 1)
    ]

    empty_edges = []

    for row, column in edges:
        if board[row][column] == "":
            empty_edges.append((row, column))

    if empty_edges:
        return random.choice(empty_edges)

    return None

if "board" not in st.session_state:
    st.session_state.board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

if "mode" not in st.session_state:
    st.session_state.mode = None

if "player" not in st.session_state:
    st.session_state.player = random.choice(["x", "o"])

if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.subheader("Choose Game Mode")

col1, col2 = st.columns(2)

with col1:
    if st.button("👥 Human VS Human", use_container_width=True):
        st.session_state.mode = "HH"
        st.session_state.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        st.session_state.player = random.choice(["x", "o"])
        st.session_state.game_over = False

with col2:
    if st.button("🤖 Human VS Computer", use_container_width=True):
        st.session_state.mode = "HC"
        st.session_state.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        st.session_state.player = "x"
        st.session_state.game_over = False

if st.session_state.mode is not None and not st.session_state.game_over:

    st.subheader(
        f"{st.session_state.player.upper()}'s Turn"
    )

    for row in range(3):

        cols = st.columns(3)

        for column in range(3):

            with cols[column]:

                if st.button(
                    st.session_state.board[row][column] or " ",
                    key=f"cell_{row}_{column}",
                    use_container_width=True
                ):
                    st.session_state.board[row][column] = st.session_state.player

                    result=check_winner()

                    if result is not None:
                        st.session_state.game_over=True
                    else:
                        if st.session_state.mode=="HC":
                            move=computer_move()

                            if move is not None:
                                comp_row,comp_col=move
                                st.session_state.board[comp_row][comp_col]="o"
                                comp_result=check_winner()
                                if comp_result is not None:
                                    st.session_state.game_over=True
                            st.session_state.player="x"

                        else:
                            if st.session_state.player=="x":
                                st.session_state.player="o"
                            else:
                                st.session_state.player="x"

                    st.rerun()

if st.session_state.game_over:
    result=check_winner()

    if result=="x":
        st.success("🎉 X Wins!")
        st.balloons()
    elif result == "o":
        st.success("🤖 O Wins!")

    elif result == "Tie":
        st.warning("🤝 It's a Tie!")

    if st.button("🔄 Play Again"):
        st.session_state.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        st.session_state.player = "x"
        st.session_state.game_over = False

        st.rerun()
