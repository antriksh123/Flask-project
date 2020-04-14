import urllib.request, json
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Example.html')

@app.route('/user', methods=['post'])
def get_corona():
    url = "https://api.covid19api.com/summary"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    user = request.form.get("user")
    user_inp = user.capitalize()
    i = 0
    isDone = False
    for a in range(0, 247):

        # This is the middle color.
        if user_inp == data.get('Countries')[i].get('Country') and data.get('Countries')[i].get('TotalConfirmed') <= 29999 and data.get('Countries')[i].get('TotalConfirmed') > 999:
            isDone = True
            country = "Country: " + str(data.get('Countries')[i].get('Country'))
            code = "Country code: " + data.get('Countries')[i].get('CountryCode')
            confirmed = "Total cases: " + str(data.get('Countries')[i].get('TotalConfirmed'))
            deaths_tot = "Total deaths: " + str(data.get('Countries')[i].get('TotalDeaths'))
            recov = "Total recoveries: " + str(data.get('Countries')[i].get('TotalRecovered'))
            new_conf = "New cases: " + str(data.get('Countries')[i].get('NewConfirmed'))
            die = "New deaths: " + str(data.get('Countries')[i].get('NewDeaths'))
            reco = "New recoveries: " + str(data.get('Countries')[i].get('NewRecovered'))
            return render_template("Example.html", country=country, code=code, total_confirm=confirmed, total_deaths=deaths_tot, total_recov=recov, new_confirm=new_conf, new_die=die, new_reco=reco)

        # This is the lightest color.
        elif user_inp == data.get('Countries')[i].get('Country') and data.get('Countries')[i].get('TotalConfirmed') < 999:
            isDone = True
            country = "Country: " + str(data.get('Countries')[i].get('Country'))
            code = "Country code: " + data.get('Countries')[i].get('CountryCode')
            confirmed = "Total cases: " + str(data.get('Countries')[i].get('TotalConfirmed'))
            deaths_tot = "Total deaths: " + str(data.get('Countries')[i].get('TotalDeaths'))
            recov = "Total recoveries: " + str(data.get('Countries')[i].get('TotalRecovered'))
            new_conf = "New cases: " + str(data.get('Countries')[i].get('NewConfirmed'))
            die = "New deaths: " + str(data.get('Countries')[i].get('NewDeaths'))
            reco = "New recoveries: " + str(data.get('Countries')[i].get('NewRecovered'))
            return render_template("Example.html", ccountry=country, ccode=code, ctotal_confirm=confirmed,
                                   ctotal_deaths=deaths_tot, ctotal_recov=recov, cnew_confirm=new_conf, cnew_die=die,
                                   cnew_reco=reco)

        # This is the darkest color.
        elif user_inp == data.get('Countries')[i].get('Country') and data.get('Countries')[i].get('TotalConfirmed') >= 30000:
            isDone = True
            country = "Country: " + str(data.get('Countries')[i].get('Country'))
            code = "Country code: " + data.get('Countries')[i].get('CountryCode')
            confirmed = "Total cases: " + str(data.get('Countries')[i].get('TotalConfirmed'))
            deaths_tot = "Total deaths: " + str(data.get('Countries')[i].get('TotalDeaths'))
            recov = "Total recoveries: " + str(data.get('Countries')[i].get('TotalRecovered'))
            new_conf = "New cases: " + str(data.get('Countries')[i].get('NewConfirmed'))
            die = "New deaths: " + str(data.get('Countries')[i].get('NewDeaths'))
            reco = "New recoveries: " + str(data.get('Countries')[i].get('NewRecovered'))
            return render_template("Example.html", dccountry=country, dccode=code, dctotal_confirm=confirmed,
                                   dctotal_deaths=deaths_tot, dctotal_recov=recov, dcnew_confirm=new_conf, dcnew_die=die,
                                   dcnew_reco=reco)
        else:
            i += 1
    if isDone == False:
        return render_template("Example.html", error="The data for the country entered does not exist.")


if __name__ == '__main__':
    app.run()