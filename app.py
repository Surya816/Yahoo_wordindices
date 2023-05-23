from flask import Flask, render_template
from pymongo import MongoClient
import json
import io
import base64

app = Flask(__name__)

client = MongoClient("mongodb+srv://bskk816:bskk816@cluster0.uuc5f0g.mongodb.net/")
db = client['yahoo']

def find_index_of_value(lst, value):
    for index, dictionary in enumerate(lst):
        if value in dictionary.values():
            return index
    return -1  # Value not found

@app.route('/')
def display_collection():
    # Connect to MongoDB
    
    collection = db['symbols_table']

    # Fetch data from the collection
    data = collection.find()

    # Render the HTML template with the data
    return render_template('index.html', data=data)

@app.route('/data/<symbol>')
def retrun_data(symbol):
    sym_collec  = db['symbols_table']
    sym_data = list(sym_collec.find())
    i = find_index_of_value(sym_data, symbol)
    if i != -1:
        summary_location = "Summary_collection"+str(i+1)
        # print(summary_location)
        collection = db[summary_location]

        # Fetch data from the collection
        data1 = collection.find()
        print(data1)
        doc = list(data1)
        # del doc[0]['_id']

        Historical_location = "Historic_collection" + str(i+1)

        collection = db[Historical_location]
        data2 = collection.find()
        doc2 = list(data2)
        # print(doc2)


        image_data = "chart" + str(i+1)

        collection = db[image_data]
        data3 = collection.find()
        doc3 = list(data3)

    

        image_data = doc3[0]["image"]
        # image_data = collection.find_one()['image']

        


        encoded_image = base64.b64encode(image_data).decode('utf-8')




        return  render_template('index copy.html', data=doc,data2 = doc2,image = encoded_image)
    





    else:
        return {}

if __name__ == '__main__':
    app.run(debug=True)

