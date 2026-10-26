from flask import Flask, render_template, request, redirect, url_for

app = Flask(
    __name__,
    template_folder='Templates',
    static_folder='Static'
)

# =====================================
# STUDENT TRACKER DATA
# =====================================

students = [
    {"nama": "Devon", "nilai": 90},
    {"nama": "Farrel", "nilai": 84}
]


# =====================================
# HOME
# =====================================

@app.route('/')
def index():
    return render_template('index.html')

# =====================================
# ABOUT
# =====================================

@app.route('/about')
def about():
    return render_template('about.html')


# =====================================
# PROJECT
# =====================================

@app.route('/project')
def project():
    return render_template('project.html')


# =====================================
# CONTACT
# =====================================

@app.route('/contact')
def contact():
    return render_template('contact.html')


# ==============================
# EDUHUB CREATIVE SUITE
# ==============================

@app.route('/eduhub')
def eduhub():
    return render_template('eduhub_creative_suite_pelajar.html')


# =====================================
# EDULAB INTERACTIVE SIMULATION SUITE
# =====================================

@app.route('/edulab')
def edulab():
    return render_template('edulab_interactive_simulation_suite.html')


# =====================================
# TASKSCHOOL DASHBOARD
# =====================================

@app.route('/taskschool_dashboard')
@app.route('/taskschool-dashboard')
def taskschool_dashboard():
    return render_template('taskschool_dashboard.html')


# =====================================
# BACKWARD-COMPATIBLE ENDPOINTS
# =====================================

# Endpoint dashboard lama
app.add_url_rule(
    '/taskschool_dashboard',
    endpoint='dashboard',
    view_func=taskschool_dashboard
)

# Mengakomodasi salah ketik endpoint yang muncul
# pada error BuildError sebelumnya.
app.add_url_rule(
    '/taskschool_dashboard',
    endpoint='taskschool_dashbaasrd',
    view_func=taskschool_dashboard
)


# Route lama /todo tetap dapat digunakan
@app.route('/todo')
def todo():
    return redirect(url_for('taskschool_dashboard'))


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == '__main__':
    app.run(debug=True)
