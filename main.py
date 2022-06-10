import sys 
from flask import Flask, response , Request


if len(sys.argv) > 1:
    mode = sys.argv[1]
else :
    print('Missing required arguments testing/production')
    exit()



if mode == 'testing':
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif mode == 'production':
    import bjoern
    bjoern.run(app, "0,0,0", 5000)
else :
    print('Invalid mode, must be one of: testing/production')