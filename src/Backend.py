from flask import Flask, render_template, request,flash,redirect
import folium
from branca.element import Figure
import main

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

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
    listJalan = []
    if (request.form.get("pilihkota")):
        if (pilihankota == 2) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("ITB.txt")
        elif (pilihankota == 3) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("Alunalun.txt")
        elif (pilihankota == 4) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("buahbatu.txt")
        elif (pilihankota == 5) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("Kebumen.txt")
        elif (pilihankota == 6) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("graf.txt")
        elif (pilihankota == 7) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("tayu.txt")
        elif (pilihankota == 8) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("blitar.txt")
        elif (pilihankota == 9) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("monas.txt")
        if request.method == 'POST':
            if (pilihankota == 1):
                fig5=Figure(height=550,width=750)
                m5=folium.Map(location=[-6.920817, 107.604100],tiles='cartodbpositron',zoom_start=17)
                fig5.add_child(m5)
                folium.LayerControl().add_to(m5)
                m5.save('templates/map.html')
                flash('Masukkan Map Kota Anda', "info")
                return render_template('GoogleMaps.html')
        fig5=Figure(height=550,width=750)
        middle = main.middlePoint(listCoor)
        m5=folium.Map(location=[middle[0],middle[1]],tiles='cartodbpositron',zoom_start=17)
        fig5.add_child(m5)
        f1=folium.FeatureGroup("Jalan Asli")
        for i in range(len(listCoor)-1):
            
            for j in range(i+1, len(listCoor)):
                if (adjMatrix[i][j] != 0):
                    place1 = [[listCoor[i][0],listCoor[i][1]],[listCoor[j][0],listCoor[j][1]]]
                    line_1=folium.vector_layers.PolyLine(place1,color='red',weight=10).add_to(f1)

        #bikin node
        for i in range(len(listCoor)):
            folium.Marker(listCoor[i],popup=listNode[i],tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='blue',icon='none')).add_to(m5)
        
        f1.add_to(m5) 
        folium.LayerControl().add_to(m5)
        m5.save('templates/map.html')
        return render_template('GoogleMaps.html', comp_select = str(pilihankota))
    
    if (request.form.get("search")):
        if (pilihankota == 2) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("ITB.txt")
            path, isNodeFound, isPathFound = main.main(adjMatrix,listNode,listCoor,firstloc,endloc)
        elif (pilihankota == 3) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("Alunalun.txt")
            path, isNodeFound, isPathFound = main.main(adjMatrix,listNode,listCoor,firstloc,endloc)
        elif (pilihankota == 4) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("buahbatu.txt")
            path, isNodeFound, isPathFound = main.main(adjMatrix,listNode,listCoor,firstloc,endloc)
        elif (pilihankota == 5) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("Kebumen.txt")
            path, isNodeFound, isPathFound = main.main(adjMatrix,listNode,listCoor,firstloc,endloc)
        elif (pilihankota == 6) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("graf.txt")
            path, isNodeFound, isPathFound = main.main(adjMatrix,listNode,listCoor,firstloc,endloc)
        elif (pilihankota == 7) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("tayu.txt")
            path, isNodeFound, isPathFound = main.main(adjMatrix,listNode,listCoor,firstloc,endloc)
        elif (pilihankota == 8) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("blitar.txt")
            path, isNodeFound, isPathFound = main.main(adjMatrix,listNode,listCoor,firstloc,endloc)
        elif (pilihankota == 9) :
            adjMatrix, listNode, listCoor, isFileFound = main.bacaFile("monas.txt")
            path, isNodeFound, isPathFound = main.main(adjMatrix,listNode,listCoor,firstloc,endloc)
        if request.method == 'POST':
            if (pilihankota == 1):
                fig5=Figure(height=550,width=750)
                m5=folium.Map(location=[-6.920817, 107.604100],tiles='cartodbpositron',zoom_start=17)
                fig5.add_child(m5)
                folium.LayerControl().add_to(m5)
                m5.save('templates/map.html')
                flash('Masukkan Map Kota Anda')
                return render_template('GoogleMaps.html')
            
            elif (not isNodeFound): #cek flag nodefound
                fig5=Figure(height=550,width=750)
                middle = main.middlePoint(listCoor)
                m5=folium.Map(location=[middle[0], middle[1]],tiles='cartodbpositron',zoom_start=17)
                fig5.add_child(m5)
                f1=folium.FeatureGroup("Jalan Asli")
                for i in range(len(listCoor)-1):
                    for j in range(i+1, len(listCoor)):
                        if (adjMatrix[i][j] != 0):
                            place1 = [[listCoor[i][0],listCoor[i][1]],[listCoor[j][0],listCoor[j][1]]]
                            line_1=folium.vector_layers.PolyLine(place1,color='red',weight=10).add_to(f1)
                for i in range(len(listCoor)):
                    folium.Marker(listCoor[i],popup=listNode[i],tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='blue',icon='none')).add_to(m5)
                f1.add_to(m5) 
                folium.LayerControl().add_to(m5)
                m5.save('templates/map.html')
                flash('Tidak ditemukan lokasi yang sesuai')
                return render_template('GoogleMaps.html', comp_select = str(pilihankota))
            elif (not isPathFound):
                fig5=Figure(height=550,width=750)
                middle = main.middlePoint(listCoor)
                m5=folium.Map(location=[middle[0], middle[1]],tiles='cartodbpositron',zoom_start=17)
                fig5.add_child(m5)
                f1=folium.FeatureGroup("Jalan Asli")
                for i in range(len(listCoor)-1):
                    for j in range(i+1, len(listCoor)):
                        if (adjMatrix[i][j] != 0):
                            place1 = [[listCoor[i][0],listCoor[i][1]],[listCoor[j][0],listCoor[j][1]]]
                            line_1=folium.vector_layers.PolyLine(place1,color='red',weight=10).add_to(f1)
                for i in range(len(listCoor)):
                    folium.Marker(listCoor[i],popup=listNode[i],tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='blue',icon='none')).add_to(m5)
                f1.add_to(m5) 
                folium.LayerControl().add_to(m5)
                m5.save('templates/map.html')
                flash('Tidak ditemukan jalan menuju lokasi tujuan')
                return render_template('GoogleMaps.html',comp_select = str(pilihankota))
            else:
                for i in range(len(path)-1):
                    listJalan.append([listCoor[path[i]],listCoor[path[i+1]]])
                    
                fig5=Figure(height=550,width=750)
                middle = main.middlePoint(listCoor)
                m5=folium.Map(location=[middle[0],middle[1]],tiles='cartodbpositron',zoom_start=17)
                fig5.add_child(m5)
                f1=folium.FeatureGroup("Jalan Asli")
                for i in range(len(listCoor)-1):
                    for j in range(i+1, len(listCoor)):
                        if (adjMatrix[i][j] != 0):
                            place1 = [[listCoor[i][0],listCoor[i][1]],[listCoor[j][0],listCoor[j][1]]]
                            line_1=folium.vector_layers.PolyLine(place1,color='red',weight=10).add_to(f1)
                
                
                
                jarakpath = "Jaraknya " + str(main.hitungJarakPath(adjMatrix,path,listCoor)) + " meter"
                for i in range(len(listJalan)):
                    line_1=folium.vector_layers.PolyLine(listJalan[i],popup=jarakpath,tooltip=jarakpath,color='blue',weight=10).add_to(f1)
                
                #bikin node
                for i in range(len(listCoor)):
                    folium.Marker(listCoor[i],popup=listNode[i],tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='blue',icon='none')).add_to(m5)
                
                for i in range(len(path)):
                    folium.Marker(listCoor[path[i]],popup=listNode[path[i]],tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='green',icon='none')).add_to(m5)
                
                f1.add_to(m5) 
                folium.LayerControl().add_to(m5)
                m5.save('templates/map.html')

    #kalau sampai sini aman
    #bisa mulai gambar

    #untuk ngecek apakah node i dan j dihubungkan 1 sisi atau gak -> cek adjMatrix[i][j] jika isinya 0 berarti gak berhubungan
    #untuk cek coordinat simpul ke i dari listNode tinggal pilih listCoor[i] (isinya tuple, yang pertama lat kedua long)
    #harusnya bisa lah ya kan alam gitu lho hehe
    
    #ini buat nampilin pake panah2 gitu jadi maneh gk usah liat
    #nah kalau mau hitung jaraknya bisa pake ini hitungJarakPath, jaraknya dalam meter
    
    return render_template('GoogleMaps.html')

if __name__ == '__main__':
    app.run(debug=True)