from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    # Example projects data
    projects_data = [
        {
            'title': 'Web Development Showcase',
            'description': 'Built a responsive website showcasing my web development skills using HTML, CSS, and JavaScript.',
            'link': 'https://github.com/kbromg15'
        },
        {
            'title': 'Data Analysis Tool',
            'description': 'Developed a data analysis tool using Python and Pandas for processing and visualizing datasets.',
            'link': 'https://github.com/yourusername/data-analysis-tool'
        },
        {
            'title': 'Diabetes Predictions',
        'description': 'Implemented a machine learning model to predict diabetes based on relevant features. Utilized Python, scikit-learn, and data preprocessing techniques.',
        'link': 'https://github.com/yourusername/diabetes-predictions'
            
        },
        # Add more projects as needed
    ]
    return render_template('projects.html', projects=projects_data)
#add route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
