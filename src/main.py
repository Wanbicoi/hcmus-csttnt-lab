from utils.readfiles import read_files
from utils.handle import handle
import os


if __name__ == "__main__":
    graphs = read_files()  # [[Graph x 5], [Graph x 3], [Graph x 3]]
    handle(graphs, "src/output/")