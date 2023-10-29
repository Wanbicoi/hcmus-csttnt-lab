import matplotlib.pyplot as plt
import os


def save_fig_visualization(matrix, bonus, start, end, save_file_path: str, route=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    # 1. Define walls and array of direction based on the route
    walls = [
        (i, j)
        for i in range(len(matrix))
        for j in range(len(matrix[0]))
        if matrix[i][j] == "x"
    ]

    if route:
        direction = []
        for i in range(1, len(route)):
            if route[i][0] - route[i - 1][0] > 0:
                direction.append("v")  # ^
            elif route[i][0] - route[i - 1][0] < 0:
                direction.append("^")  # v
            elif route[i][1] - route[i - 1][1] > 0:
                direction.append(">")
            else:
                direction.append("<")

        direction.pop(0)

    # 2. Drawing the map
    ax = plt.figure(dpi=100).add_subplot(111)

    for i in ["top", "bottom", "right", "left"]:
        ax.spines[i].set_visible(False)

    plt.scatter(
        [i[1] for i in walls], [-i[0] for i in walls], marker="X", s=100, color="black"
    )

    plt.scatter(
        [i[1] for i in bonus], [-i[0] for i in bonus], marker="P", s=100, color="green"
    )

    plt.scatter(start[1], -start[0], marker="*", s=100, color="gold")

    if route:
        for i in range(len(route) - 2):
            plt.scatter(
                route[i + 1][1], -route[i + 1][0], marker=direction[i], color="silver"
            )

    plt.text(
        end[1],
        -end[0],
        "EXIT",
        color="red",
        horizontalalignment="center",
        verticalalignment="center",
    )
    os.makedirs(os.path.dirname(save_file_path), exist_ok=True)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(save_file_path + "/" + os.path.basename(save_file_path)+ ".jpg", format="jpg")
