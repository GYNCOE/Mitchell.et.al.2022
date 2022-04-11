import os
import xml.etree.ElementTree as ET

def createXML(address):
    
    for y in os.listdir(address):
        try:
            if ".py" in y: continue
            calip =[]
            already = 0

            # find out if XML file has already been generated and skip folder
            for p in os.listdir(os.path.join(address, y)):
                if ".xml" in p:
                    already += 1
            if already > 0:
                continue

            # continue if XML file is not in folder
            
            for x in os.listdir(os.path.join(address, y)):
                if ".annotations" in x and "calib" in x:
                    fullname = os.path.join(os.path.join(address, y),x)
                    tree1 = ET.parse(fullname)
                    root1 = tree1.getroot()
                
                    for child in root1.iter("Vertices"):
                        for x in child.iter("V"):
                            ex = x.get("X").strip()
                            wy = x.get("Y").strip()
                            calip.append([ex,wy])
                            break


            for x in os.listdir(os.path.join(address, y)):
                if ".annotations" in x and "calib" not in x:
                    fullname = os.path.join(os.path.join(address, y),x)
                    tree = ET.parse(fullname)
                    root = tree.getroot()
               
            #### Count the Number of elements from the root object ####
                    cnt = 0
                    for y in root.iter("Vertices"):
                        cnt += 1


                    #### Count all the point in each shape ####
                    shpln = {}
                    ctp = 0
                    for child in root.iter("Vertices"):
                        ct = 0
                        ctp += 1
                        for x in child.iter("V"):
                            ct += 1
                        shpln[ctp] = ct


            #### Create XML document and start adding the global points ####       

                    output = open("{}.xml".format(fullname),"w")
                    output.write("<ImageData>")
                    output.write("\n")
                    output.write("<GlobalCoordinates>1</GlobalCoordinates>")
                    output.write("\n")    
                    output.write("<X_CalibrationPoint_1>{}</X_CalibrationPoint_1>".format(calip[0][0]))
                    output.write("\n")
                    output.write("<Y_CalibrationPoint_1>{}</Y_CalibrationPoint_1>".format(calip[0][1]))
                    output.write("\n")
                    output.write("<X_CalibrationPoint_2>{}</X_CalibrationPoint_2>".format(calip[1][0]))
                    output.write("\n")
                    output.write("<Y_CalibrationPoint_2>{}</Y_CalibrationPoint_2>".format(calip[1][1]))
                    output.write("\n")
                    output.write("<X_CalibrationPoint_3>{}</X_CalibrationPoint_3>".format(calip[2][0]))
                    output.write("\n")
                    output.write("<Y_CalibrationPoint_3>{}</Y_CalibrationPoint_3>".format(calip[2][1]))
                    output.write("\n")
                    output.write("<ShapeCount>{}</ShapeCount>".format(cnt))
                    output.write("\n")

                    num = 0
                    for child in root.iter("Vertices"):
                        num += 1
                        nmel = 0
                        output.write("<Shape_{}>".format(num))
                        output.write("\n")
                        output.write("<PointCount>{}</PointCount>".format(shpln[num]))
                        output.write("\n")


                        for x in child.iter("V"):
                            ex = x.get("X").strip()
                            wy = x.get("Y").strip()
                            output.write("<X_{}>{}</X_{}>".format(nmel + 1,ex,nmel + 1))
                            output.write("\n")
                            output.write("<Y_{}>{}</Y_{}>".format(nmel + 1,wy,nmel + 1))
                            output.write("\n")
                            nmel += 1
                                        
                        output.write("</Shape_{}>".format(num))
                        output.write("\n")

                    output.write("</ImageData>")   
                    output.close()
        except:
            print("Unable to generate .XML import for {}".format(y))
            continue
      
                      
createXML(r"\\wh-nas.whirc.local\aperio-storage-1\Images\JOVE\PTSD")
