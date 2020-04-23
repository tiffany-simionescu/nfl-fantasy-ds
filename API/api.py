"""
Data science API application that analyzes and gives scores for 
nfl fantasy football player trades.
"""


from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from .errors import InvalidUsage
from .data import data
from .data import week1


load_dotenv()
def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def root():
        """
        Root page, you should not land here.
        """
        return render_template('home.html')

    @app.route("/api/trade/", methods=['GET'])
    def analyze_trade():
        """
        API main route, takes in player IDs and returns predictions
        """
        player0_id = request.args.get('player0_id')
        player1_id = request.args.get('player1_id')
        player2_id = request.args.get('player2_id')
        player3_id = request.args.get('player3_id')
        player4_id = request.args.get('player4_id')
        player5_id = request.args.get('player5_id')
        player6_id = request.args.get('player6_id')
        player7_id = request.args.get('player7_id')
        player8_id = request.args.get('player8_id')
        player9_id = request.args.get('player9_id')
        week = request.args.get('week')

        if request.method == 'GET':
            if not 'player0_id' in request.args:
                raise InvalidUsage(message = "request argument 'player0_id=' missing")
            if not 'player1_id' in request.args:
                raise InvalidUsage(message = "request argument 'player1_id=' missing")
            if not 'week' in request.args:
                raise InvalidUsage(message = "request argument 'week=' missing")
            if 'week' in request.args:
                if week != "1":
                    raise InvalidUsage(message = "only week 1 predictions available")

        if week == "1":
            request_args = [player0_id, player1_id]
            results = week1[week1.index.isin(request_args)]
            json = results.to_json(orient='table')
        
        return json

    @app.errorhandler(404)
    def page_not_found(error):
        return 'This page does not exist', 404

    @app.errorhandler(InvalidUsage)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app

if __name__ == "__main__":
    """
    Bind to PORT if defined, otherwise default to 5000.
    """
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)