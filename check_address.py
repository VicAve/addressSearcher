from flask import Flask, render_template, request, redirect, escape, send_from_directory, url_for
from find_process import checkAddress
from werkzeug import secure_filename
import time
import os

#   Initiates the Flusk's app
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'


# Function that writes info into log file
def log_request(address, lng, lat):
   with open('log.log', 'a') as log:
       time_now = time.ctime()
       print('Modified at:', time)
       print(time_now, address, lng, lat, file=log, end='\n', sep='|')

@app.route('/')
def main() -> 'html':
    return render_template('welcome.html')

@app.route('/upload',methods=['POST'])
def upload():
    print('uploaded')
    contents = []
    with open('uploads/dir', 'r') as dir:
            for line in dir:
                print('')
                result = checkAddress(line)
                if result:
                    print(len(result),'founded!')
                    for reg in result:
                        print(reg['address'],reg['lng'],reg['lat'])
                        log_request(reg['address'],reg['lng'],reg['lat'])
                    contents.append(result[0])
                else:
                    log_request(line, 'Was not found','...')
                    resulted={'address': line, 'reqAddr': False}
                    contents.append(resulted)



            return render_template('results2.html', the_results = contents)



    #***********************************************
    #Fake entry of archive, because of permissions in my windows server of shit!
    # file = request.files['fileAddress']
    # filename = secure_filename(file.filename)
    # file.save(os.path.join(app.config['UPLOAD_FOLDER']), filename)
    # address_to_search='cool'
    # return render_template('base.html',the_title = address_to_search)

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

@app.route('/search',methods=['POST'])
def do_search() -> 'html':
    address_to_search = request.form['address']
    result = checkAddress(address_to_search)
    no_founded = len(result)
    if no_founded > 0:
        print(no_founded,'founded!')
        for reg in result:
            print(reg['address'],reg['lng'],reg['lat'])
            log_request(reg['address'],reg['lng'],reg['lat'])
    else:
        log_request(address_to_search, 'Was not found','...')

    return render_template('results.html',the_address = address_to_search, the_results = result, the_number = no_founded)

if __name__ == '__main__':
     app.run(debug=True)
