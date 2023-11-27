from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

contacts = [
    {
        'name': 'John Doe',
        'address': '123 Main St',
        'profession': 'Engineer',
        'tel_number': '123-456-7890',
        'email': 'john@example.com',
        'password': 'securepass'
    }
]

@app.route('/')
def index():
    return render_template('create_contact.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        profession = request.form['profession']
        tel_number = request.form['tel_number']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('index'))

        new_contact = {
            'name': name,
            'address': address,
            'profession': profession,
            'tel_number': tel_number,
            'email': email,
            'password': password
        }
        contacts.append(new_contact)
        flash('Contact added successfully!', 'success')
        return redirect(url_for('index'))

    return 'Invalid request'

@app.route('/view_contacts')
def view_contacts():
    return render_template('view_contacts.html', contacts=contacts, enumerate=enumerate)

@app.route('/update_contact/<int:index>', methods=['GET', 'POST'])
def update_contact(index):
    if request.method == 'GET':
        contact = contacts[index]
        return render_template('update_contact.html', contact=contact, index=index)
    elif request.method == 'POST':
        contacts[index]['name'] = request.form['name']
        contacts[index]['address'] = request.form['address']
        contacts[index]['profession'] = request.form['profession']
        contacts[index]['tel_number'] = request.form['tel_number']
        contacts[index]['email'] = request.form['email']
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('view_contacts'))

@app.route('/delete_contact/<int:index>', methods=['POST'])
def delete_contact(index):
    del contacts[index]
    flash('Contact deleted successfully!', 'success')
    return redirect(url_for('view_contacts'))

if __name__ == '__main__':
    app.run(debug=True)