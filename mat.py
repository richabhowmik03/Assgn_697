import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

# Dataset for basic plot
x = [1, 2, 3]
y = [4, 5, 6]

# Dataset for bar graph and horizontal bar graph, pie chart and exploded pie chart
languages = ["English", "Spanish", "Japanese", "French"]
students = [50,23,41,19]
explode = [0.3, 0, 0, 0]

# Dataset for line graph
yplots = np.array([10, 4, 5, 1, 8])

# Dataset for scatter plot
scatter_x = np.array([3, 11, 8, 4, 10, 7, 6, 1, 9, 2])
scatter_y = np.array([78, 91, 81, 90, 86, 99, 84, 89, 82, 95])

# Dataset for multiple lines
x1 = [1,2,3]
y1 = [7,8,9]
x2 = [1,2,3]
y2 = [4,5,6]

# Dataset for
def basic_plot():
    plt.plot(x, y)
    plt.show()


def bar_graph():
    plt.bar(languages, students)
    plt.title("Bar graph data for Language spoken by students")
    plt.xlabel("Language Spoken")
    # plt.ylabel("Number of student")
    plt.show()


def horizontal_bar_graph():
    plt.barh(languages, students)
    plt.style.use("seaborn-dark")
    plt.title("Horizontal bar graph for language spoken by students")
    plt.show()


def line_graph():
    plt.plot(yplots, linestyle="dashdot")
    plt.show()


def scatter_plot():
    plt.scatter(scatter_x, scatter_y)
    plt.show()


def pie_chart():
    plt.pie(students, labels = languages)
    plt.show()


def exploded_pie_chart():
    plt.pie(students, labels=languages, explode=explode)
    plt.show()


def multiple_lines():
    plt.plot(x1, y1, label = "First Line")
    plt.plot(x2, y2, label = "Second Line")

    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Multiple lines")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # basic_plot()
    # horizontal_bar_graph()
    # line_graph()
    # scatter_plot()
    # pie_chart()
    # exploded_pie_chart()
    multiple_lines()
