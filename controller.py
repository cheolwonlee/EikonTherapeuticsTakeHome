from flask import Flask
import db_connector as db

app = Flask(__name__)

@app.route('/db/init')
def initialize_db():
    db.import_from_file("./data/users.csv","users")
    db.import_from_file("./data/compounds.csv","compounds")
    db.import_from_file("./data/user_experiments.csv","user_experiments")
    return 'Database initialized'

@app.route('/user/<user>/experiments/')
def get_total_experiments(user):
    user = user.capitalize()
    experiments_for_user = db.get_experiments_for_user(user)
    if experiments_for_user>0:
        return "The user {0} has run {1} experiments".format(user,experiments_for_user)
    else:
        return "The user {0} has no experiments.".format(user)

@app.route('/user/<user>/average_experiments/')
def get_average_experiments(user):
    user = user.capitalize()
    average_experiments = db.get_average_amount_per_user(user)    
    return "The user {0}'s experiments have an average run time of {1}.".format(user,average_experiments)

    
@app.route('/user/<user>/compound')
def get_users_most_commonly_used_compound(user):
    user = user.capitalize()
    compounds = db.get_users_most_commonly_used_compound(user)
    if len(compounds) == 1:
        return "The user {0}'s most used compound is: {1}".format(user,compounds[0])
    elif len(compounds)>1:
        return "The user {0}'s most used compounds are: {1}".format(user,compounds)
    else:
        return "The user {0} has no compounds.".format(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
   