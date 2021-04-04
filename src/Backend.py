from flask import Flask, render_template, request
import folium
from branca.element import Figure
import main

app = Flask(__name__)

@app.route('/')
def index():
    fig5=Figure(height=550,width=750)
    m5=folium.Map(location=[-6.920817, 107.604100],tiles='cartodbpositron',zoom_start=17)
    fig5.add_child(m5)

    adjMatrix = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],[1, 0, 1, 0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],[1, 0, 0, 0, 0, 1, 0, 0, 1, 0],[0, 0, 0, 0, 1, 0, 1, 0, 0, 1],[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],[0, 0, 0, 1, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 1, 0, 0, 1, 0]]
    listCoor = [(-6.920817, 107.604100),(-6.920893, 107.605089),(-6.921052, 107.606472),(-6.921228,107.607690),(-6.922083, 107.604024),(-6.922383, 107.606429),(-6.922521,107.607099),(-6.922551, 107.607520),(-6.923107, 107.603929),(-6.923423, 107.606288)]
    f1=folium.FeatureGroup("Place 1")
    for i in range(len(listCoor)-1):
        for j in range(i+1, len(listCoor)):
            if (adjMatrix[i][j] != 0):
                place1 = [[listCoor[i][0],listCoor[i][1]],[listCoor[j][0],listCoor[j][1]]]
                line_1=folium.vector_layers.PolyLine(place1,popup='<b>Path of Place 1</b>',tooltip='Place 1',color='blue',weight=10).add_to(f1)
    


    
    

    
    f1.add_to(m5)
    folium.LayerControl().add_to(m5)
    m5.save('templates/map.html')
    return render_template('GoogleMaps.html')

@app.route('/', methods = ['POST'])
def getvalue():
    firstloc = request.form['floc']
    endloc = request.form['eloc']
    return render_template('GoogleMaps.html', firstloc=firstloc, endloc=endloc)

    
@app.route('/', methods = ['POST'])
def getform():
    kota2 = request.form['city']
    return render_template('GoogleMaps.html', firstloc=firstloc, endloc=endloc)
    
@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/register' , methods=['POST'])
def test():
    firstloc = request.form['floc']
    endloc = request.form['eloc']
    learning_style = request.form.get("comp_select")
    return render_template('GoogleMaps.html', kota = learning_style, firstloc = firstloc, endloc= endloc)

if __name__ == '__main__':
    app.run(debug=True)