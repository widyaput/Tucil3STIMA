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
    folium.LayerControl().add_to(m5)
    m5.save('templates/map.html')
    return render_template('GoogleMaps.html')
  
@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/register' , methods=['POST'])
def test():
    firstloc = request.form['floc']
    endloc = request.form['eloc']
    pilihankota = int(request.form.get("comp_select"))
    adjMatrix = [[]]
    listNode = []
    listCoor = []
    if (pilihankota == 1) :
        print("masuk")
        adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("Alunalun.txt")
    

    #kalau sampai sini aman
    #bisa mulai gambar

    #untuk ngecek apakah node i dan j dihubungkan 1 sisi atau gak -> cek adjMatrix[i][j] jika isinya 0 berarti gak berhubungan
    #untuk cek coordinat simpul ke i dari listNode tinggal pilih listCoor[i] (isinya tuple, yang pertama lat kedua long)
    #harusnya bisa lah ya kan alam gitu lho hehe
    
    #ini buat nampilin pake panah2 gitu jadi maneh gk usah liat
    #nah kalau mau hitung jaraknya bisa pake ini hitungJarakPath, jaraknya dalam meter
    
    fig5=Figure(height=550,width=750)
    m5=folium.Map(location=[listCoor[0][0],listCoor[0][1]],tiles='cartodbpositron',zoom_start=17)
    fig5.add_child(m5)
    
    f1=folium.FeatureGroup("Jalan Asli")
    for i in range(len(listCoor)-1):
        
        for j in range(i+1, len(listCoor)):
            if (adjMatrix[i][j] != 0):
                place1 = [[listCoor[i][0],listCoor[i][1]],[listCoor[j][0],listCoor[j][1]]]
                line_1=folium.vector_layers.PolyLine(place1,popup='<b>Path of Jalan Asli</b>',tooltip='Jalan Asli',color='red',weight=10).add_to(f1)
    
    #bikin node
    for i in range(len(listCoor)):
        folium.Marker(listCoor[i],popup=listNode[i],tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='red',icon='none')).add_to(m5)
    
    f1.add_to(m5) 
    folium.LayerControl().add_to(m5)
    m5.save('templates/map.html')
    return render_template('GoogleMaps.html', kota = pilihankota, firstloc = firstloc, endloc= endloc)

if __name__ == '__main__':
    app.run(debug=True)