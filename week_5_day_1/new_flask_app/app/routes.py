from app import app
from flask import render_template

@app.route('/')
def homepage():
    fighter_stats = {"Jon Jones":{"url":"https://dmxg5wxfqgb4u.cloudfront.net/styles/athlete_bio_full_body/s3/2020-09/JONES_JON_L_12-29.png?VersionId=_V_SgUOaxjt7ja7ddhcJB4m9ALbyeMJz&itok=kMklO45v", "description":"Jon Jones, the best MMA fighter of all time."},
                    "Anderson Silva":{"url":"https://qph.cf2.quoracdn.net/main-qimg-1257c6e43e3b85f1e47b1deee45c88d4-lq", "description":"Anderson Silva, once believed to be the GOAT."}, 
                    "Conor McGregor":{"url":"https://dmxg5wxfqgb4u.cloudfront.net/styles/athlete_bio_full_body/s3/2021-07/MCGREGOR_CONOR_L_07-10.png?itok=xbg9Kwfj", "description":"Conor McGregor, the biggest star in MMA history."},
                    "Stephen Thompson":{"url":"https://dmxg5wxfqgb4u.cloudfront.net/styles/athlete_bio_full_body/s3/2022-12/THOMPSON_STEPHEN_L_12-03.png?itok=Ix8SmbJQ", "description":"Stephen Thompson, the nicest mother effer in MMA history."},
                    "Joe Rogan":{"url":"https://pyxis.nymag.com/v1/imgs/244/e39/98f4597712a76c23d84f2719beca4fbf44-12-joe-rogan.rsquare.w700.jpg", "description":"Joe Rogan, the best commentator in MMA history."}}
    # fighter_descriptions = ["Jon Jones, the best MMA fighter of all time.",
    #                 "Anderson Silva, once believed to be the GOAT.", 
    #                 "Conor McGregor, the biggest star in MMA history.", 
    #                 "Stephen Thompson, the nicest mother effer in MMA history.",
    #                 "Joe Rogan, the best commentator in MMA history."]
    return render_template('index.html', fighters = fighter_stats)

@app.route('/random_page')
def random_page():
    return render_template('random_page.html')