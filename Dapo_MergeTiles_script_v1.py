
def HALO(ebe):
    import os
    import xml.etree.ElementTree as ET

    #### Grab global point from calibration file ####

    
    tree = ET.parse("{}.annotations".format(ebe))
    root = tree.getroot()

#### Create XML document and start adding the global points ####       

    output = open("{}_merged.annotations".format(ebe),"w")
    output.write("<Annotations>")
    output.write("\n")
    output.write('  <Annotation LineColor="65280" Name="Tile 1" Visible="True">')
    output.write("\n")    
    output.write("    <Regions>")
    output.write("\n")


    num = 0
    for child in root.iter("Vertices"):
        num += 1
        nmel = 0
        output.write('      <Region Type="Polygon" HasEndcaps="0" NegativeROA="0">')
        output.write("\n")
        output.write("        <Vertices>")
        output.write("\n")


        for x in child.iter("V"):
            ex = x.get("X").strip()
            wy = x.get("Y").strip()
            output.write('         <V X="{}" Y="{}" />'.format(ex, wy))
            output.write("\n")
                        
        output.write("        </Vertices>")
        output.write("\n")
        output.write("        <Comments />")
        output.write("\n")
        output.write("      </Region>")
        output.write("\n")


    output.write("    </Regions>")
    output.write("\n")
    output.write('  </Annotation>')
    output.write("\n")
    output.write("</Annotations>")

HALO("JoveTest")


