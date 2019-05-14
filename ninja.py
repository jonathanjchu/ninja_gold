from flask import Flask, render_template, request, redirect, session
import datetime, random

app = Flask(__name__)
app.secret_key = "WMWeQ*x&u*ldQN06Bv^nt2o&Bk*wJ%He"

# game_data = {
#     'farm': {
#         min: 10,
#         max: 20
#     }
# }

@app.route("/")
def index():
    if 'gold' not in session:
        session['gold'] = 0

    return render_template("index.html")


@app.route("/gold_dig", methods=['POST'])
def gold_dig():
    # get activities
    if 'activities' in session:
        activities = session['activities']
    else:
        activities = ""
    
    if 'gold' in session:
        gold = session['gold']
    else:
        gold = 0
    
    output = ""
    income = 0
    prefix = ""

    # check location
    if request.form['location'] == "farm":
        income = random.randint(10, 20)
        output += f"earned {income} from farming"
    elif request.form['location'] == 'cave':
        income = random.randint(5, 10)
        output += f"earned {income} exploring cave"
    elif request.form['location'] == 'house':
        income = random.randint(2, 5)
        output += f"earned {income} breaking and entering house"
    elif request.form['location'] == 'casino':
        income = random.randint(-50, 50)
        if income > 0:
            output += f"earned {income} gambling at casino"
        elif income < 0:
            output += f"lost {income*-1} gambling at casino"
        else:
            output += "broke even while gambling at casino"

    if income > 0:
        prefix = '<div class="green">'
    elif income < 0:
        prefix = '<div class="red">'
    else:
        prefix = "<div>"

    gold += income
    session['gold'] = gold

    current_time = datetime.datetime.now().strftime(" (%Y-%b-%d %H:%M:%S)</div>")
    session['activities'] = prefix + output + current_time + activities

    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
