from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def check_password_strength(password):
    strength = {
        'message': '',
        'className': ''
    }

    if len(password) < 6:
        strength['message'] = 'Too short'
        strength['className'] = 'strength-weak'
    elif len(password) < 8:
        strength['message'] = 'Weak'
        strength['className'] = 'strength-weak'
    else:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_number = any(c.isdigit() for c in password)
        has_special = any(c in '!@#$%^&*(),.?":{}|<>' for c in password)

        passed_checks = [has_upper, has_lower, has_number, has_special].count(True)

        if passed_checks >= 3:
            if len(password) >= 12:
                strength['message'] = 'Strong'
                strength['className'] = 'strength-strong'
            else:
                strength['message'] = 'Good'
                strength['className'] = 'strength-good'
        else:
            strength['message'] = 'Fair'
            strength['className'] = 'strength-fair'

    return strength

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.json.get('password')
    strength = check_password_strength(password)
    return jsonify(strength)

if __name__ == '__main__':
    app.run(debug=True)
