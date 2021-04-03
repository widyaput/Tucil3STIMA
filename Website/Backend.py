from flask import Flask, render_template, request
import folium
from branca.element import Figure

app = Flask(__name__)

@app.route('/')
def index():
    fig5=Figure(height=550,width=750)
    m5=folium.Map(location=[-6.887221,107.611479],tiles='cartodbpositron',zoom_start=17)
    fig5.add_child(m5)
    place1 = [[-6.887221,107.611479],[-6.884972,107.611512]]
    f1=folium.FeatureGroup("Place 1")
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