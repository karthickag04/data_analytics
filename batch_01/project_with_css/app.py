from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

# Load dataset (Iris dataset from seaborn)
def load_data():
    iris = sns.load_dataset("iris")
    return iris

# Generate Matplotlib Chart
def create_chart(iris):
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
    plt.title("Sepal Length vs Width")
    chart_path = os.path.join("static", "chart.png")
    plt.savefig(chart_path)
    plt.close()

@app.route('/')
def index():
    # Load and process the dataset
    iris = load_data()

    # Create the chart
    create_chart(iris)

    # Calculate basic stats
    summary = iris.describe()

    return render_template('index.html', tables=[summary.to_html(classes='data')], titles=summary.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
