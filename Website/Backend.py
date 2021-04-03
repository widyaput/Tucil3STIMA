from flask import Flask, render_template
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

@app.route('/map')
def map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)